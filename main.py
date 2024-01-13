# 타이핑 게임 제작
# 2023 12 23 

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from gui import TypingGameGUI
import sound
import database
import random
import time

class TypingGame:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.gui = TypingGameGUI()

        # 게임 초기화
        self.words = []
        self.load_words()
        self.n = 1
        self.cor_cnt = 0
        self.start = None
        self.is_paused = False
        self.remaining_time = 0

        # 타이머 설정
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)
        self.remaining_time = 0
        # GUI 이벤트 연결
        self.gui.start_button.clicked.connect(self.start_game)
        self.gui.answer_input.returnPressed.connect(self.check_answer)
        self.gui.pause_button.clicked.connect(self.pause_game)
        self.gui.exit_button.clicked.connect(self.exit_game)

        self.gui.show()
        sys.exit(self.app.exec_())

    def load_words(self):
        with open('./resource/word.txt') as f:
            for c in f:
                self.words.append(c.strip())

    def start_game(self):
        difficulty = self.gui.difficulty_selector.currentText()
        if difficulty == "쉬움":
            self.time_limit = 30
        elif difficulty == "보통":
            self.time_limit = 15
        elif difficulty == "어려움":
            self.time_limit = 5

        self.start = time.time()
        self.n = 1
        self.cor_cnt = 0
        self.remaining_time = self.time_limit
        self.next_question()
        self.timer.start(1000)
        self.update_timer_label()

    def pause_game(self):
        if self.is_paused:
            self.timer.start()
            self.is_paused = False
        else:
            self.timer.stop()
            self.is_paused = True

    def exit_game(self):
        sys.exit(0)

    def next_question(self):
        if self.n <= 5:
            random.shuffle(self.words)
            q = random.choice(self.words)
            self.gui.set_question_text("Question # {}: {}".format(self.n, q))
            self.gui.answer_input.clear()
            self.remaining_time = self.time_limit
        else:
            self.end_game()

    def check_answer(self):
        answer = self.gui.answer_input.text()
        question = self.gui.question_label.text().split(": ")[1]

        if answer.strip() == question.strip():
            sound.play_sound('correct')
            self.cor_cnt += 1
        else:
            sound.play_sound('wrong')

        self.n += 1
        self.next_question()

    def end_game(self):
        self.timer.stop()
        end = time.time() - self.start
        end = format(end, ".3f")
        result = "합격!" if self.cor_cnt >= 3 else "불합격!"
        database.insert_record(self.cor_cnt, end)
        self.gui.set_question_text("게임 종료: {}\n게임 시간: {}초, 정답 개수: {}".format(result, end, self.cor_cnt))

    def update_game(self):
        if not self.is_paused:
            self.remaining_time -= 1
            self.gui.set_timer_text("남은 시간: {}초".format(self.remaining_time))

            if self.remaining_time <= 0:
                sound.play_sound('wrong')  # 시간 초과 시 오답 소리 재생
                self.n += 1
                if self.n > 5:
                    self.end_game()
                else:
                    self.next_question()


if __name__ == "__main__":
    TypingGame()