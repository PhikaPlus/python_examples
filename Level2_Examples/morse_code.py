import winsound
import time

# Morse codes sounds
def dot():
    winsound.Beep(428, 300)

def dash():
    winsound.Beep(428, 700)

sleep_after_words = 1
def play(str):
    a = str


    def p():
        dot()
        time.sleep(0.2)
        dash()
        time.sleep(0.2)
        dash()
        time.sleep(0.2)
        dot()
        time.sleep(sleep_after_words)

    def i():
        dot()
        time.sleep(0.2)
        dot()
        time.sleep(sleep_after_words)

    def h():
        dot()
        time.sleep(0.2)
        dot()
        time.sleep(0.2)
        dot()
        time.sleep(0.2)
        dot()
        time.sleep(sleep_after_words)

    def k():
        dash()
        time.sleep(0.2)
        dot()
        time.sleep(0.2)
        dash()
        time.sleep(sleep_after_words)

    def a():
        dot()
        time.sleep(0.2)
        dash()
        time.sleep(sleep_after_words)

    p()
    h()
    i()
    k()
    a()


play('phika')
