#ddos原生清洗 集群管理
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from func.base import Base
import allure


class Ddos_cluster(Base):
    @allure.step('点击新建集群')
    def click_new_cluster(self):
        #点击新增集群
        self.find_element('xpath','//span[text()="新增集群"]/..').click()

    @allure.step('点击配置设备')
    def click_configure_device(self, cluster_name):
        #点击配置设备
        self.find_element('xpath','//div[contains(text(),"%s")]/ancestor::tr//a[contains(text(),"配置设备")]'%(cluster_name)).click()

    @allure.step('点击新增设备')
    def click_new_device(self, ):
        self.find_element('xpath','//span[text()="新增设备"]/..').click()

    @allure.step('填写集群表单')
    def fill_cluster_table(self, cluster_name, descp, start):
        name = self.find_element('xpath', '//label[text()="集群名称"]/following::input[@placeholder="集群名称"]')
        name.clear()
        if cluster_name != '':
            name.send_keys(cluster_name)
        description = self.find_element('xpath','//label[text()="集群名称"]/following::input[@placeholder="备注"]')
        description.clear()
        if descp != '':
            description.send_keys(descp)
        status = self.find_element('xpath','//div[@role="switch"]')
        if start != '':
            if start == 0:
                status.click()

    @allure.step('填写设备表单')
    def fill_device_table(self, device_ip, start, cpu, mem, network_card , alarm_type, alarm_person, desc):
        device_ele = self.find_element('xpath', '//input[@placeholder="0.0.0.0"]')
        device_ele.clear()
        if device_ip != '':
            device_ele.send_keys(device_ip)
        start_ele = self.find_element('xpath', '//label[text()="是否启用"]/following::div[1]//div[contains(@class,"el-switch")]')
        start_status = self.verify_attr('xpath', '//label[text()="是否启用"]/following::div[1]//div[contains(@class,"el-switch")]', 'checked', 'className')
        if start == 0 and start_status:
            start_ele.click()
        if start == 1 and not start_status:
            start_ele.click()
        cpu_ele = self.find_element('xpath', '//label[text()="CPU使用率(%)"]/following::div[1]//input')
        if cpu != '':
            cpu_ele.clear()
            cpu_ele.send_keys(cpu)
        mem_ele = self.find_element('xpath', '//label[text()="内存使用率(%)"]/following::div[1]//input')
        if mem != '':
            mem_ele.clear()
            mem_ele.send_keys(mem)
        net_ele = self.find_element('xpath',
                                      '//label[text()="网卡故障"]/following::div[1]//div[contains(@class,"el-switch")]')
        net_status = self.verify_attr('xpath',
                                        '//label[text()="网卡故障"]/following::div[1]//div[contains(@class,"el-switch")]',
                                        'checked', 'className')
        if network_card == 0 and net_status:
            net_ele.click()
        if network_card == 1 and not net_status:
            net_ele.click()
        # 预警方式
        ele_mail = self.find_element('xpath', '(//div[@aria-label="checkbox-group"]/label)[1]')
        ele_sms = self.find_element('xpath', '(//div[@aria-label="checkbox-group"]/label)[2]')
        if alarm_type != '' and alarm_type == 1:
            ele_mail.click()
        elif alarm_type != '' and alarm_type == 2:
            ele_sms.click()
        # 预警联系人
        if alarm_person != '':
            self.find_element('xpath', '//label[contains(text(),"告警联系人")]/following-sibling::div[1]//i').click()
            self.find_element('xpath',
                              '//div[contains(@class,"el-popper") and not(contains(@style,"none"))]//li[contains(text(),"%s")]' % (
                                  alarm_person)).click()
        self.find_element('xpath','//span[text()="创建设备"]').click()
        # 描述
        if desc != '':
            ele = self.find_element('xpath', '//input[@placeholder="备注"]')
            ele.clear()
            ele.send_keys(desc)

    @allure.step('点击创建集群的保存')
    def click_save(self):
        ele = self.find_element('xpath',
                                '//div[contains(@class,"DmDialog") and not(contains(@style,"none"))]/div[@aria-label="创建集群"]//span[text()="保存"]/..')
        ele.click()

    @allure.step('点击创建设备的保存')
    def click_device_save(self):
        ele = self.find_element('xpath',
                                '//div[contains(@class,"DmDialog") and not(contains(@style,"none"))]/div[@aria-label="创建设备"]//span[text()="保存"]/..',time_wait=6)
        ele.click()

    @allure.step('点击全选')
    def click_all(self):
        self.find_element('xpath','//th//span[contains(@class,"el-checkbox__input")]', time_wait=10).click()

    @allure.step('选择指定设备')
    def click_device_check_box(self, device_IP):
        self.find_element('xpath', '//div[contains(text(),"%s")]/ancestor::tr/td[1]//label'%device_IP, time_wait=10).click()

    @allure.step('点击删除')
    def click_delete(self):
        result = self.verify_attr('xpath', '//span[text()="删除"]/..', 'disabled', 'disabled')
        if result:
            assert False
        else:
            self.find_element('xpath', '//span[text()="删除"]/..').click()
            self.find_element('xpath', '//span[contains(text(),"确定")]/..').click()

    @allure.step('点击启用')
    def click_start(self):
        result = self.verify_attr('xpath', '//span[text()="启用"]/..', 'disabled', 'disabled')
        assert result == False, '无法点击启用'
        self.find_element('xpath', '//span[text()="启用"]/..').click()
        self.find_element('xpath', '//span[contains(text(),"确定")]/..').click()

    @allure.step('点击禁用')
    def click_disabled(self):
        result = self.verify_attr('xpath', '//span[text()="禁用"]/..', 'disabled', 'disabled')
        assert result == False, '无法点击禁用'
        self.find_element('xpath', '//span[text()="禁用"]/..').click()
        self.find_element('xpath', '//span[contains(text(),"确定")]/..').click()






