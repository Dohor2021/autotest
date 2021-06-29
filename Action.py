import uiautomator2 as u2
import config
import os
import time
import logging

d = u2.connect()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def clickbyResourceId(resourceid):
    """通过resourceid点击"""
    d(resourceId=resourceid).click()
    logging.debug("点击【%s】元素"%resourceid)


def cmd_adb(cmd):
    """执行cmd指令"""
    os.popen(cmd)


def catchLog():
    """抓LOG"""
    cmd_adb("adb logcat -v time -d>%s/%s.txt" % (config.Log_file, config.data))


def screencap():
    """截图"""
    data = config.data
    cmd_adb("adb shell screencap -p /data/%s.png" % data)
    time.sleep(5)
    cmd_adb("adb pull /data/%s.png %s" % (data, config.Screen_file))
    cmd_adb("adb shell rm -rf /data/%s.png")


if __name__ == "__main__":
    # clickbyResourceId("com.google.android.tvlauncher:id/banner_container")
    # catchLog()
    print(1)
