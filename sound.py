# 사운드 출력 

import winsound


def play_sound(sound_type):
    if sound_type =='correct':
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
    elif sound_type =='wrong':
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)