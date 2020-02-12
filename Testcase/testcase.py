import unittest
from Bisuness.login import Login


class Test(unittest.TestCase):
    def setUp(self):
        print('start')

    def tearDown(self):
        print('end')

    # 测试正确的用户名与密码
    def test_001(self):
        log = Login()
        log.login('**********', '********')   # 输入正确的账号密码
        # 获取登录成功后的用户名
        data = log.get_text('css', '#logined > span')
        # 断言，判断登录后的用户名是否和预期用户名相同
        self.assertEqual('**********', data) # 输入正确的账号

    # 测试正确的用户名与错误的密码
    def test_002(self):
        log = Login()
        log.login('**********', '********') # 输入正确的账号和错误的密码
        # 定位到表单，获取表单上的span元素
        log.switch_to_frame('id', 'popup_login_frame')
        data = log.get_text('id', 'Msg')
        # 断言，判断登录错误后的显示信息是否与预期信息相同
        self.assertEqual('密码错误', data) # 该预期信息与登录信息是相同的

    # 测试正确的用户名与错误的密码
    def test_003(self):
        log = Login()
        log.login('**********', '********')  # 输入正确的账号和错误的密码
        # 定位到表单，获取表单上的span元素
        log.switch_to_frame('id', 'popup_login_frame')
        data = log.get_text('id', 'Msg')
        self.assertEqual('密码', data)  # 该预期信息与登录信息是不相同的


if __name__ == '__main__':
    unittest.main()
