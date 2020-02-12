import unittest
# 导入HtmlTextRunner，用于生成html的测试报告
from Commonlib.HTMLTestRunner import HTMLTestRunner
from Testcase.testcase import Test


class SuitTest(unittest.TestCase):
    def test_suit(self):
        case_list = ['test_001', 'test_002', 'test_003']
        # 创建测试套件
        my_suit = unittest.TestSuite()
        # 循环将测试用例放进测试套件中
        for case in case_list:
            my_suit.addTest(Test(case))
        # 创建测试运行器,设置为每一个测试用例生成测试报告，运行测试套件中的测试用例
        # unittest.TextTestRunner(verbosity=2).run(mysuit)
        # 打印生成HTML测试报告
        with open('../report.html', 'wb') as f:
            HTMLTestRunner(
                stream=f,
                title='第一个测试报告',
                description='关于4399登录的测试',
                verbosity=2
            ).run(my_suit)


if __name__ == '__main__':
    unittest.main()
