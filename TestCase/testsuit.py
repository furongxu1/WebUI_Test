import unittest
from TestCase.testcase import Testcase
from Common.HTMLTestRunner import HTMLTestRunner

class Test(unittest.TestCase):
    def test_suit(self):
        # 创建测试套件
        mysuit = unittest.TestSuite()
        # 向测试套件添加测试用例
        case_list = ['test_001', 'test_002', 'test_003', 'test_004', 'test_005']
        for case in case_list:
            mysuit.addTest(Testcase(case))
        # 生成html格式测试报告
        with open('../report/report.html', 'wb') as f:
            HTMLTestRunner(
                stream=f,
                title="Selenium_UI测试报告",
                description="一号店登录页面测试",
                verbosity=2
            ).run(mysuit)


