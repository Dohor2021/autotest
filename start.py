import pytest
import config
import os
#文件名命名必须是test开头
# 不能定义init方法
# 测试函数必须test开头
#加上参数-s：显示print()函数输出的结果
#加上-v:显示每条测试案例的执行结果
log_file=config.Log_file
screen_file=config.Screen_file
os.mkdir(log_file)
os.mkdir(screen_file)
pytest.main(['-s', '-v',
             # "--junitxml=&s"%config.Report_Xml,
             # "--resultlog=%s"%config.Report_Log,
             "--html=%s"%config.Report_Html,])




