import Action
import Judge
import time
import os
from common.launcher import Launcher as L

pkg_name = "com.tcl.launcher"


class Test_launcher(object):

    def test001(self):
        print("test01")
        a = 1 + 1

        # Judge.JudgePass(a == 2)

    def test002(self):
        print("test02")

        Judge.JudgePass(1 == 1)  # 断言失败

    def test003(self):
        # Action.clickbyResourceId(L.banner_id)
        Judge.JudgePass(1 == 2)
if __name__=="__main__":
    for i in range(50):
        print("第%d次" % i)
        os.popen("adb shell input keyevent 66")
        time.sleep(8)
        os.popen("adb shell input keyevent 66")
        time.sleep(4)