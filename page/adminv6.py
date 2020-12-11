#订单管理系统 客服管理 套餐列表
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from func.base import Base
import allure
from time import sleep
from selenium.webdriver.common.by import By
class Adminv6(Base):
    @allure.step('登录v6系统')
    def login_adminv6(self,url,login_name,login_pwd):
        self.open(url)
        sleep(5)
        self.refresh()
        sleep(3)
        login_already = self.verify_element_exist('xpath','//img[@alt="logo--full"]')
        if login_already:
            print('已经登录过adminv6了')
        else:
            username = self.find_element('name','username')
            username.send_keys(login_name)
            password = self.find_element('name','password')
            password.send_keys(login_pwd)
            sleep(2)
            btn = self.find_element('xpath','//span[text()="登 录"]/..')
            btn.click()

    @allure.step('选择客服管理下的套餐列表')
    def choose_menu(self):
        self.find_element('xpath','//span[text()="客服管理"]/following::i[1]').click()
        self.find_element('xpath','//span[text()="套餐列表"]/ancestor::a[contains(@href,"advisory")]').click()
        sleep(3)

    @allure.step('根据邮箱和套餐搜索用户的套餐：邮箱{1} 套餐：Web安全加速')
    def search_mail(self,mail_address):
        self.find_element('xpath','//input[@placeholder="用户邮箱"]').send_keys(mail_address)
        sleep(1)
        self.find_element('xpath','//input[@placeholder="套餐"]/following-sibling::span//i').click()
        sleep(1)
        self.find_element('xpath','//span[text()="Web安全加速"]/preceding-sibling::label//span[1]/span').click()
        self.find_element('xpath','//input[@placeholder="套餐ID"]').click()
        sleep(2)
        self.find_element('xpath','//span[text()="搜 索"]/ancestor::button',time_wait=4).click()
        sleep(5)

    @allure.step('退订套餐并填写退订原因')
    def cancel(self):
        self.find_element('xpath','//span[contains(text(),"操作")]/ancestor::td[not(contains(@class,"is-hidden"))]//span[contains(text(),"操作")]/..').click()
        sleep(1)
        self.find_element('xpath','//ul[not(contains(@style,"display: none;"))]//div[contains(text(),"退订")]/..').click()
        sleep(2)
        self.find_element('xpath','//input[@placeholder="流失原因"]/following-sibling::span//i').click()
        sleep(1)
        self.find_element('xpath','//div[not(contains(@style,"display: none")) and contains(@class,"el-popper")]//span[text()="客户原因"]/..').click()#选择客户原因
        sleep(1)
        self.find_element('xpath','(//input[@placeholder="流失原因"])[2]/following-sibling::span//i').click()
        sleep(1)
        self.find_element('xpath','//span[text()="无需求"]/..').click()
        sleep(1)
        self.find_element('xpath','//textarea[@placeholder="请输入流失备注"]').send_keys('自动化测试退订')
        sleep(1)
        self.find_element('xpath','//div[@aria-label="套餐退订"]//span[text()="保存"]/..').click()

    @allure.step('购买高级版套餐')
    def upgrade(self,mail_address):
        self.find_element('xpath','//span[text()="开通服务"]/ancestor::a',time_wait=5).click()#点击开通服务
        sleep(1)
        self.find_element('xpath','//input[contains(@fetchsuggestions,"function")]').send_keys(mail_address)
        locator = (By.XPATH, '//i[contains(@class,"el-icon-loading")]')
        self.wait_element_invisable(locator)
        sleep(1)
        self.find_element('xpath','//ul[contains(@id,"el-autocomplete")]/li',time_wait=4).click()#点击查找出来的第一个
        locator = (By.XPATH,'//ul[contains(@id,"el-autocomplete")]/li')
        self.wait_element_invisable(locator)
        sleep(2)
        self.find_element('xpath','//form[contains(@class,"el-form form-box") and not(contains(@style,"none"))]//span[text()="下一步"]/..',time_wait=4).click()#点击下一步
        sleep(1)
        self.find_element('xpath','//input[@placeholder="开通目的"]/following-sibling::span//i',time_wait=4).click()#选择开通目的下拉
        self.find_element('xpath','//span[text()="试用开通"]/..',time_wait=4).click()#试用开通
        sleep(1)
        self.find_element('xpath', '//input[@placeholder="产品"]/following-sibling::span//i').click()  # 产品
        self.find_element('xpath', '//span[text()="Web安全加速"]/parent::li',time_wait=4).click()  # web安全加速
        sleep(1)
        self.find_element('xpath', '//input[@placeholder="套餐版本"]/following-sibling::span//i').click()  # 套餐版本
        self.find_element('xpath', '//span[text()="高级版"]/parent::li',time_wait=4).click()  # 高级版
        sleep(1)
        self.find_element('xpath', '//form[contains(@class,"el-form form-box") and not(contains(@style,"none"))]//span[text()="下一步"]/..').click()  # 点击下一步
        sleep(1)
        self.find_element('xpath','//span[text()="开通套餐"]/..').click()#点击开通套餐
        sleep(2)
        text_value = self.find_element('xpath','//div[contains(@class,"ant-result-title")]').text
        print(text_value)
        assert '操作成功' in text_value,print('操作成功！')






