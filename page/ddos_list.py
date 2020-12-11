#ddos 原生清洗 业务列表
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from func.base import Base
import allure


class Ddos_list(Base):

    @allure.step('点击菜单：{1}')
    def click_menu(self,menu_name):
        is_open_ele = self.find_element('xpath', '//span[text()="DDoS原生清洗"]/parent::div/..', time_wait=5)
        is_open = self.get_element_attr(is_open_ele, 'className')
        if 'open' not in is_open:
            self.find_element('xpath','//span[text()="DDoS原生清洗"]/following-sibling::i', time_wait=5).click()#ddos原生清洗
        self.find_element('xpath','//div[contains(@class,"FeMenuItemGroup__body")]/div[not(contains(@style,"none"))]//span[contains(text(),"%s")]/ancestor::a'%(menu_name)).click()

    @allure.step('填写防御域信息--{8}：防御域名称：{1} ;防御域IP：{2};告警阈值:{3};告警类型:{4};集群:{5};模板:{6};联系人:{7};描述:{8}')
    def fill_defence_domain(self,defence_domain_name,ips,alarm,alarm_type,cluster_name,model_name,contect,description):
        '''

        :param defence_domain_name: 防御域名称
        :param ips: 防御域IP
        :param alarm: 告警阈值
        :param alarm_type:告警类型
        :param cluster_name:集群
        :param model_name:模板
        :param contect:联系人
        :param description:描述
        :return:
        '''
        ele = self.find_element('xpath','//input[@placeholder="域名称"]')
        ele.clear()
        if defence_domain_name != '':
            ele.send_keys(defence_domain_name)#防御域名称
        ele = self.find_element('xpath','//textarea[@placeholder="0.0.0.0"]')
        ele.clear()
        if ips != '':
            ele.send_keys(ips)#防御域IP地址
        ele = self.find_element('xpath','//input[@aria-label="描述文字"]')
        ele.clear()
        if alarm != '':
            ele.send_keys(alarm)#告警阈值
        #预警方式
        ele_mail = self.find_element('xpath','(//div[@aria-label="checkbox-group"]/label)[1]')
        ele_sms = self.find_element('xpath','(//div[@aria-label="checkbox-group"]/label)[2]')
        if alarm_type != '' and alarm_type == 1:
            ele_mail.click()
        elif alarm_type != '' and alarm_type == 2:
            ele_sms.click()
        #清洗设备集群
        if cluster_name != '':
            self.find_element('xpath', '//label[contains(text(),"清洗设备集群")]/following-sibling::div[1]//i').click()
            self.find_element('xpath','//div[contains(@class,"el-popper") and not(contains(@style,"none"))]//li[contains(text(),"%s")]' % (
                                               cluster_name)).click()
        #配置模板
        if model_name != '':
            self.find_element('xpath', '//label[contains(text(),"引用配置模板")]/following-sibling::div[1]//i').click()
            self.find_element('xpath','//div[contains(@class,"el-popper") and not(contains(@style,"none"))]//li[contains(text(),"%s")]' % (
                                               model_name)).click()
        #预警联系人
        if contect != '':
            self.find_element('xpath', '//label[contains(text(),"告警联系人")]/following-sibling::div[1]//i').click()
            self.find_element('xpath',
                              '//div[contains(@class,"el-popper") and not(contains(@style,"none"))]//li[contains(text(),"%s")]' % (
                                  contect)).click()
        #描述
        if description != '':
            ele = self.find_element('xpath','//input[@placeholder="描述"]')
            ele.clear()
            ele.send_keys(description)

    @allure.step('点击新增防御域')
    def click_new_domain(self):
        self.find_element('xpath', '//span[text()="新增防御域"]/..').click()

    @allure.step('点击修改防御域')
    def click_modify_domain(self):
        self.find_element('xpath', '//span[text()="修改"]/..').click()

    @allure.step('点击添加子域')
    def click_new_child_domain(self):
        self.find_element('xpath', '//span[text()="添加子域"]/..').click()

    @allure.step('点击策略配置')
    def click_modify_conf(self, defence_domain_name):
        self.find_element('xpath', '//div[text()="%s"]/../..//span[text()="策略配置"]/..'%(defence_domain_name)).click()


    @allure.step('点击创建防御域的保存')
    def click_save(self):
        ele = self.find_element('xpath','//div[contains(@class,"DmDialog") and not(contains(@style,"none"))]/div[@aria-label="创建防御域"]//span[text()="保存"]/..')
        ele.click()
        # result = self.get_success_message('操作成功')


    @allure.step('点击创建防御域的取消')
    def click_cancel(self):
        ele = self.find_element('xpath',
                                '//div[contains(@class,"DmDialog") and not(contains(@style,"none"))]/div[@aria-label="创建防御域"]//span[text()="取消"]/..')
        ele.click()










