# 타이핑 게임 gui 
# PyQt5

import sys
from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget,QApplication,QComboBox
from PyQt5.QtCore import QTimer

class TypingGameGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # 중앙 위젯과 레이아웃 설정
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.difficulty_selector = QComboBox(self)
        self.difficulty_selector.addItems(["쉬움","보통","어려움"])
        layout.addWidget(self.difficulty_selector)

        # 문제 문자 표시 영역
        self.question_label = QLabel(self)
        layout.addWidget(self.question_label)

        # 텍스트 입력 상자
        self.answer_input = QLineEdit(self)
        layout.addWidget(self.answer_input)

        # 타이머 표시 
        self.timer_label = QLabel("00:00", self)
        layout.addWidget(self.timer_label)

        # 점수 표시 
        self.score_label = QLabel("점수 : 0", self)
        layout.addWidget(self.score_label)

        # 제어 버튼
        self.start_button = QPushButton("시작", self)
        layout.addWidget(self.start_button)

        self.pause_button = QPushButton("정지", self)
        layout.addWidget(self.pause_button)

        self.exit_button = QPushButton("종료",self)
        layout.addWidget(self.exit_button)


        # 창 설정
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("타이핑 게임")

    def set_question_text(self, text):
        # 문제를 받아와 전달 
        self.question_label.setText(text)

    def set_answer_input(self, input_text):
        # 입력한 문자 전달
        self.answer_input.setText(input_text)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = TypingGameGUI()
    mainWindow.show()
    sys.exit(app.exec_())
