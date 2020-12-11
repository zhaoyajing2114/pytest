import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())
print(sys.path)
from page.login_page import Login_page
from selenium import webdriver
from time import sleep
import allure
import pytest
@pytest.mark.page
@allure.feature('登录')
class Test_login:
    # @pytest.fixture(scope='function')
    # def get_page(self):
    #     driver = webdriver.Chrome()
    #     self.page = Login_page(driver)
    #     yield
    #     driver.quit()
    driver = webdriver.Chrome()
    page = Login_page(driver)
    @allure.story('正确的用户名和密码进行登录')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success(self):
        self.page.open('https://www.yundun.com/login')
        sleep(2)
        ele = self.page.find_element('xpath','//a[text()="继续登录主账号"]')
        if ele:
            ele.click()
        self.page.type_username('zhaoyajing@yundun.com')
        self.page.type_password('4726586z.')
        sleep(1)
        self.page.click_login_button()
        sleep(0.1)
        self.page.assert_login_success()

    @allure.story('不正确的用户名和密码进行登录')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("name,pwd", [('zhaoyajing@yundun.com','123')#正确用户名错误的密码
        ,('123','4726586z.')#错误用户名正确的密码
        ,('123','123')#错误用户名错误的密码
        ,('','4726586z.')#不填用户名，正确的密码
        ,('zhaoyajing@yundun.com','')#正确的用户名，不填密码
                                          ])
    def test_login_fail(self,name,pwd):
        self.page.open('https://www.yundun.com/login')
        sleep(2)
        self.page.type_username(name)
        self.page.type_password(pwd)
        sleep(1)
        self.page.click_login_button()
        sleep(0.5)
        self.page.assert_login_fail()
