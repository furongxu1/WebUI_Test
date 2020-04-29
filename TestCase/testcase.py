import unittest
from Business.Login import Login

class Testcase(unittest.TestCase):
    def setup(self):
        print("start")

    def tearDown(self):
        print("end")

    def test_001(self):
        # 登录成功的情况
        log = Login()
        log.login('xufurong', '1234567')
        # 获取用于断言判断的登录后用户名
        data = log.get_text('class', 'hd_login_name')
        # 断言判断
        self.assertEqual('xufurong', data)

    def test_002(self):
        # 账号密码为空
        log = Login()
        log.login('', '')
        # 获取登录后的错误提示元素
        data = log.get_text('id', 'error_tips')
        # 断言判断
        self.assertEqual('请输入账号和密码', data)

    def test_003(self):
        # 密码为空
        log = Login()
        log.login('xufurong', '')
        # 获取登录后的错误提示元素
        data = log.get_text('id', 'error_tips')
        # 断言判断
        self.assertEqual('请输入密码', data)

    def test_004(self):
        # 账号密码错误
        log = Login()
        log.login('17287893', '19288789')
        # 获取登录后的错误提示元素
        data = log.get_text('id', 'error_tips')
        # 断言判断
        self.assertEqual('账号和密码不匹配，请重新输入', data)

    def test_005(self):
        # 账号密码错误
        log = Login()
        log.login('17287893', '19288789')
        # 获取登录后的错误提示元素
        data = log.get_text('id', 'error_tips')
        # 断言失败判断
        self.assertEqual('账号密码不对，重新输入', data)

