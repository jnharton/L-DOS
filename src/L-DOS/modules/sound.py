import winsound

'''
'''
def PlayBeep(p, d):
    winsound.Beep(p, d)


def PlaySound(filename):
    winsound.PlaySound(filename, winsound.SND_FILENAME)


def invalid_beep():
    winsound.Beep(700,1000)


def confirm_beep():
    winsound.Beep(1600,100)


def error_beep():
    winsound.Beep(1200,1500)