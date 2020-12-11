#ddos原生清洗 配置模板
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from func.base import Base
import allure


class Ddos_model(Base):

    @allure.step('填写创建模板表单：模板名称-{1}，描述-{2}，复制模板-{3}')
    def fill_model(self,model_name, description, copy_mpdel):
        name = self.find_element('xpath','//input[@placeholder="模板名称"]', time_wait=4)
        if model_name != '':
            name.clear()
            name.send_keys(model_name)
        desc = self.find_element('xpath','//input[@placeholder="描述"]')
        if description != '':
            desc.clear()
            desc.send_keys()
        if copy_mpdel != '':
            self.find_element('xpath','//label[text()="复制模板"]/following-sibling::div//i').click()
            self.find_element('xpath','//div[contains(@class,"el-popper") and not(contains(@style,"none"))]//li[contains(text(),"%s")]'%(copy_mpdel)).click()

    @allure.step('点击新增配置模板')
    def click_new_model(self):
        self.find_element('xpath','//span[text()="新增配置模板"]/..').click()

    @allure.step('点击创建配置模板的保存')
    def click_save(self):
        ele = self.find_element('xpath','//div[contains(@class,"DmDialog") and not(contains(@style,"none"))]/div[@aria-label="创建模板"]//span[text()="保存"]/..')
        ele.click()

    @allure.step('点击策略配置')
    def click_modify_conf(self,model_name):
        self.find_element('xpath', '//tr/td/div[text()="%s"]/../..//a[text()="策略配置"]'%(model_name)).click()