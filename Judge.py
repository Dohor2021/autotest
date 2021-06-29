import Action
import time

def JudgePass(msg):
    try:
        assert msg
        if msg is True:
            pass
    except:
        Action.screencap()
        time.sleep(5)
        Action.catchLog()


