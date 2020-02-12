import time

from selenium import webdriver


class CommonShare(object):

    # 初始化
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    # 打开网页
    def open_url(self, url):
        self.driver.get(url)
        time.sleep(3)

    # 元素定位
    def locate_element(self, locate_type, value):
        el = None
        if locate_type == 'id':
            el = self.driver.find_element_by_id(value)
        elif locate_type == 'name':
            el = self.driver.find_element_by_name(value)
        elif locate_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == 'tag':
            el = self.driver.find_element_by_tag_name(value)
        elif locate_type == 'css':
            el = self.driver.find_element_by_css_selector(value)
        elif locate_type == 'text':
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == 'class':
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == 'partial':
            el = self.driver.find_element_by_partial_link_text(value)

        if el is not None:
            return el

    # 点击操作
    def click(self, locate_type, value):
        el = self.locate_element(locate_type, value)
        el.click()

    # 向元素输入内容
    def input_data(self, locate_type, value, data):
        el = self.locate_element(locate_type, value)
        el.send_keys(data)

    # 获取元素文本内容
    def get_text(self, locate_type, value):
        el = self.locate_element(locate_type, value)
        return el.text

    # 获取元素属性值
    def get_attr(self, locate_type, value, data):
        el = self.locate_element(locate_type, value)
        return el.get_attribute(data)

    # 定位到表单
    def switch_to_frame(self, locate_type, value):
        el = self.locate_element(locate_type, value)
        self.driver.switch_to.frame(el)

    # 删除对象释放空间
    def __del__(self):
        time.sleep(3)
        self.driver.quit()


'''
if __name__ == '__main__':
    com = CommonShare()
    com.open_url('http://www.baidu.com')
    com.input_data('id', 'kw', 'selenium')
    com.click('id', 'su')
    time.sleep(3)
'''
if __name__ == '__main__':
    pass
