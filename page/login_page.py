import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))

from func.base import Base
import allure
class Login_page(Base):
    @allure.step('打开网站：{1}')
    def open_url(self,url):
        self.open(url)
    @allure.step('输入用户名:{1}')
    def type_username(self,value):
        ele = self.find_element('id','username')
        ele.clear()
        ele.send_keys(value)

    @allure.step('输入密码:{1}')
    def type_password(self,value):
        ele = self.find_element('id', 'password')
        ele.clear()
        ele.send_keys(value)

    @allure.step('点击登录按钮')
    def click_login_button(self):
        self.find_element('xpath','//button[@type="submit"]').click()

    @allure.step('校验登录成功！')
    def assert_login_success(self):
        assert self.verify_text('xpath','//div[@class="ant-message"]//span//span','登录成功') == True#登录提示内容是“登录成功”
        assert self.verify_element_exist('xpath', '//a[@class="logo"]') == True  # 登录提示

    @allure.step('校验登录失败！')
    def assert_login_fail(self):
        assert self.verify_element_not_exist('css','.ya-phone-fill',3) == True#登录提示