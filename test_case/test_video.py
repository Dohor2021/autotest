import pytest

#文件名命名必须是test开头
# 不能定义init方法
# 测试函数必须test开头

class TestLoginCase(object):

     # def __init__(self):

    def test001(self):
        print("test01")
        a=1+1

        assert a==2

    def test002(self):
        print("test02")

        assert 1==2  #断言失败

# if __name__ == '__main__':
#     #pytest.main(['test01.py'])
#
#     #加上参数-s：显示print()函数输出的结果
#     #加上-v:显示每条测试案例的执行结果
#     pytest.main(['-s','-v','test.py'
#                  ,"--html=./test.html"])

