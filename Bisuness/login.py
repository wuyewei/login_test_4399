from Commonlib.commonlib import CommonShare


class Login(CommonShare):

    def login(self, user, psw):
        self.open_url('http://www.4399.com/')
        self.click('id', 'login_tologin')
        # 需要定位到表单才可以获取输入框
        self.switch_to_frame('id', 'popup_login_frame')
        self.input_data('id', 'username', user)
        self.input_data('id', 'j-password', psw)
        self.click('css', 'input.ptlogin_btn')
        # 退出表单，返回到主页面
        self.driver.switch_to.default_content()

