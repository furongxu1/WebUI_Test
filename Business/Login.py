from Common.Commonlib import CommonShare

class Login(CommonShare):
    def login(self, user, pwd):
        # 跳转到一号店
        self.open_url('http://www.yhd.com')
        # 点击登录按钮
        self.click('class', 'hd_login_link')
        # 登录框输入数据
        self.input_data('id', 'un', user)
        # 密码框输入数据
        self.input_data('id', 'pwd', pwd)
        # 点击登录按钮
        self.click('id', 'login_button')

