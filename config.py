"""全局变量"""
import time
data=time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
Log_file="./log/log%s"%data
Report_Html="./report/%s.html"%data
Report_Xml="./report/%s.xml"%data
Report_Log="./report/%s.txt"%data
Device_id=""
Screen_file="./screen/%s"%data
# print(Screen_file)