#ddos 原生清洗 配置模板
import sys
import os
import allure
sys.path.append(os.path.dirname(os.getcwd()))
from func.base import Base

class Ddos_conf(Base):

    @allure.step('返回当前tcp连接阻断的状态')
    def get_drop_tcp_all_switch(self):
        return self.find_element('xpath',
            '//h2[contains(text(),"连接阻断")]/../following-sibling::div[contains(@class,"action")]//input').text  # 值

    @allure.step('tcp连接阻断')
    def click_drop_tcp_all_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath','//h2[contains(text(),"连接阻断")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath','//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..'%(statue)).click()

    @allure.step('返回当前源站学习的状态')
    def get_src_station_auto_learn_switch(self):
        return self.find_element('xpath',
                                 '//h2[contains(text(),"源站学习")]/../following-sibling::div[contains(@class,"action")]//input').text  # 值

    @allure.step('源站学习')
    def click_src_station_auto_learn_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"源站学习")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('返回当前目的IP TCP限速的状态')
    def get_tcp_bps_limit_switch(self):
        ele = self.find_element('xpath',
                                 '//h2[contains(text(),"目的IP TCP限速")]/../following-sibling::div[contains(@class,"action")]//input')  # 值
        return self.get_element_attr(ele, 'value')

    @allure.step('返回目的IP tcp限速的值')
    def get_tcp_bps_limit(self):
        ele = self.find_element('xpath','//h2[contains(text(),"目的IP TCP限速")]/../following::form[1]//input')
        return self.get_element_attr(ele, 'value')

    @allure.step('目的IP TCP限速')
    def click_tcp_bps_limit_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"目的IP TCP限速")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('修改目的IP tcp限速的值')
    def modify_tcp_bps_limit(self, tcp_bps_limit):
        ele = self.find_element('xpath', '//h2[contains(text(),"目的IP TCP限速")]/../following::form[1]//input')
        ele.clear()
        ele.send_keys(tcp_bps_limit)

    @allure.step('返回当前源IP TCP限速的状态')
    def get_src_pps_limit_switch(self):
        ele = self.find_element('xpath',
                                 '//h2[contains(text(),"源IP TCP限速")]/../following-sibling::div[contains(@class,"action")]//input')  # 值
        return self.get_element_attr(ele , 'value')

    @allure.step('返回源IP TCP限速的值')
    def get_src_pps_limit(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"源IP TCP限速")]/../following::form[1]//input')
        return self.get_element_attr(ele, 'value')

    @allure.step('源IP TCP限速')
    def click_src_pps_limit_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"目的IP TCP限速")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('修改目的IP tcp限速的值')
    def modify_src_pps_limit(self, tcp_bps_limit):
        ele = self.find_element('xpath', '//h2[contains(text(),"目的IP TCP限速")]/../following::form[1]//input')
        ele.clear()
        ele.send_keys(tcp_bps_limit)

    @allure.step('返回当前TCP异常报文防御的状态')
    def get_tcp_abnormal_switch(self):
        ele = self.find_element('xpath',
            '//h2[contains(text(),"TCP异常报文防御")]/../following-sibling::div[contains(@class,"action")]//input')  # 值
        return self.get_element_attr(ele, 'value')

    @allure.step('TCP异常报文防御')
    def click_tcp_abnormal_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"TCP异常报文防御")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('修改TCP Flag 非法防御')
    def modify_tcp_flag_invalid_protect_switch(self):
        self.find_element('xpath', '//h2[contains(text(),"TCP异常报文防御")]/../following::label[contains(@class,"el-checkbox")][1]/span/span').click()

    @allure.step('获取TCP Flag 非法防御是否被选择')
    def get_tcp_flag_invalid_protect_switch(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"TCP异常报文防御")]/../following::label[contains(@class,"el-checkbox")][1]/span')
        class_value = self.get_element_attr(ele, 'class')
        if 'checked' in class_value:
            return True
        else:
            return False

    @allure.step('修改SYN包 非法防御')
    def modify_tcp_flag_invalid_protect_switch(self):
        self.find_element('xpath',
                          '//h2[contains(text(),"TCP异常报文防御")]/../following::label[contains(@class,"el-checkbox")][2]/span/span').click()

    @allure.step('获取SYN包 非法防御是否被选择')
    def get_tcp_flag_invalid_protect_switch(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"TCP异常报文防御")]/../following::label[contains(@class,"el-checkbox")][1]/span')
        class_value = self.get_element_attr(ele,'className')
        if 'checked' in class_value:
            return True
        else:
            return False

#syn flood 防御
    @allure.step('获取包速率阈值')
    def get_syn_pps_threshold(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//label[text()="包速率阈值"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改包速率阈值')
    def modify_syn_pps_threshold(self, syn_pps_threshold):
        ele = self.find_element('xpath',
            '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//label[text()="包速率阈值"]/following::input[1]')
        ele.clear()
        ele.send_keys(syn_pps_threshold)

    @allure.step('获取认证方式')
    def get_syn_protection_alg(self):
        rigth_seq = self.find_element('xpath', '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//label[text()="认证方式"]/following::span[contains(text(),"right-seq")]/..')
        error_seq = self.find_element('xpath', '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//label[text()="认证方式"]/following::span[contains(text(),"error-seq")]/..')
        right_class_value = self.get_element_attr(rigth_seq, 'className')
        error_class_value = self.get_element_attr(error_seq, 'className')
        if 'checked' in right_class_value:
            return 0
        if 'checked' in error_class_value:
            return 1

    @allure.step('修改认证方式')
    def modify_syn_protection_alg(self, syn_protection_alg):
        rigth_seq = self.find_element('xpath',
                                      '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//label[text()="认证方式"]/following::span[contains(text(),"right-seq")]/..//input')
        error_seq = self.find_element('xpath',
                                      '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//label[text()="认证方式"]/following::span[contains(text(),"error-seq")]/..//input')
        if syn_protection_alg == 0:
            rigth_seq.click()
        else:
            error_seq.click()

    @allure.step('获取 目的IP SYN报文限速')
    def get_syn_pps_limit(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//label[text()="目的IP SYN报文限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改 目的IP SYN报文限速')
    def modify_syn_pps_limit(self, syn_pps_limit):
        ele = self.find_element('xpath', '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//label[text()="目的IP SYN报文限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(syn_pps_limit)

    @allure.step('获取 源IP SYN报文限速')
    def get_src_syn_pps_limit(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//label[text()="源IP SYN报文限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改 源IP SYN报文限速')
    def modify_src_syn_pps_limit(self, src_syn_pps_limit):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//label[text()="源IP SYN报文限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(src_syn_pps_limit)

    @allure.step('修改 动态黑名单开关')
    def modify_dynamic_black_white_list_switch(self, dynamic_black_white_list_switch):
        checked_status = False
        ele = self.find_element('xpath', '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//span[text()="源IP加入黑名单"]/../span[1]')
        checked = self.get_element_attr(ele, 'className')
        if 'checked' in checked:
            checked_status = True
        if dynamic_black_white_list_switch == 0 and checked_status:
            ele.click()
        if not checked_status and dynamic_black_white_list_switch == 1:
            ele.click()

    @allure.step('获取动态黑白名单状态')
    def get_dynamic_black_white_list_switch(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//span[text()="源IP加入黑名单"]/../span[1]')
        checked = self.get_element_attr(ele, 'className')
        if 'checked' in checked:
            return True
        else:
            return False

    @allure.step('获取加入黑名单的单位时间 配合syn包数量最大值')
    def get_src_syn_stats_time(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//span[text()="秒（范围：0-60）"]/preceding-sibling::div[1]//input')
        return self.get_element_attr(ele, 'value')

    @allure.step('修改加入黑名单的单位时间 配合syn包数量最大值')
    def modify_src_syn_stats_time(self, src_syn_stats_time):
        ele = self.find_element('xpath', '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//span[text()="秒（范围：0-60）"]/preceding-sibling::div[1]//input')
        ele.clear()
        ele.send_keys(src_syn_stats_time)

    @allure.step('获取 加入黑名单的SYN包数量最大值')
    def get_src_syn_pps_max(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//span[text()="SYN包数量（范围：0-1,000,000）"]/preceding-sibling::div[1]//input')
        return self.get_element_attr(ele, 'value')

    @allure.step('修改加入黑名单的SYN包数量最大值')
    def modify_src_syn_pps_max(self, src_syn_pps_max):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN Flood 防御")]/../following::form[1]//span[text()="SYN包数量（范围：0-1,000,000）"]/preceding-sibling::div[1]//input')
        ele.clear()
        ele.send_keys(src_syn_pps_max)

    @allure.step('获取SYN-ACK Flood 防御 包速率阈值')
    def get_syn_ack_pps_threshold(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[1]//label[text()="包速率阈值"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改SYN-ACK Flood 防御 包速率阈值')
    def modify_syn_ack_pps_threshold(self, src_syn_pps_limit):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[1]//label[text()="包速率阈值"]/following::input[1]')
        ele.clear()
        ele.send_keys(src_syn_pps_limit)

    @allure.step('获取SYN-ACK Flood 防御 包速率限速')
    def get_syn_ack_pps_limit(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[1]//label[text()="包速率限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改SYN-ACK Flood 防御 包速率限速')
    def modify_syn_ack_pps_limit(self, src_syn_pps_limit):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[1]//label[text()="包速率限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(src_syn_pps_limit)

    @allure.step('获取 SYN-ACK Flood 防御 目的端口过滤')
    def get_syn_ack_port_filter_switch(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[2]//span[text()="目的端口过滤"]/../span[1]')
        class_value = self.get_element_attr(ele, 'className')
        if 'checked' in class_value:
            return 1
        else:
            return 0

    @allure.step('修改 SYN-ACK Flood 防御 目的端口过滤')
    def modify_syn_ack_port_filter_switch(self, syn_ack_port_filter_switch):
        swtich_status = False
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[2]//span[text()="目的端口过滤"]/../span[1]')
        class_value = self.get_element_attr(ele, 'className')
        if 'checked' in class_value:
            swtich_status = True
        if swtich_status and syn_ack_port_filter_switch == 0:
            ele.click()
        if not swtich_status and syn_ack_port_filter_switch == 1:
            ele.click()

    @allure.step('获取目的端口过滤最小值')
    def get_syn_ack_port_start(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[2]//span[text()="最小值"]/preceding-sibling::div[1]//input')
        return self.get_element_attr(ele, 'value')

    @allure.step('修改目的端口过滤最小值')
    def modify_syn_ack_port_start(self, syn_ack_port_start):
        ele = self.find_element('xpath', '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[2]//span[text()="最小值"]/preceding-sibling::div[1]//input')
        ele.clear()
        ele.send_keys(syn_ack_port_start)

    @allure.step('获取目的端口过滤最大值')
    def get_syn_ack_port_end(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[2]//span[text()="最大值"]/preceding-sibling::div[1]//input')
        return self.get_element_attr(ele, 'value')

    @allure.step('修改目的端口过滤最大值')
    def modify_syn_ack_port_end(self, syn_ack_port_end):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[2]//span[text()="最大值"]/preceding-sibling::div[1]//input')
        ele.clear()
        ele.send_keys(syn_ack_port_end)

    @allure.step('获取 SYN-ACK Flood 防御 增强防御')
    def get_syn_ack_enhance_protection_switch(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[2]//span[text()="增强防御"]/../span[1]')
        class_value = self.get_element_attr(ele, 'className')
        if 'checked' in class_value:
            return 1
        else:
            return 0

    @allure.step('修改 SYN-ACK Flood 防御 增强防御')
    def modify_syn_ack_enhance_protection_switch(self, syn_ack_enhance_protection_switch):
        swtich_status = False
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[2]//span[text()="增强防御"]/../span[1]')
        class_value = self.get_element_attr(ele, 'className')
        if 'checked' in class_value:
            swtich_status = True
        if swtich_status and syn_ack_enhance_protection_switch == 0:
            ele.click()
        if not swtich_status and syn_ack_enhance_protection_switch == 1:
            ele.click()

    @allure.step('获取 SYN-ACK Flood 防御	增强防御阈值')
    def get_syn_ack_enhance_pps_threshold(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[2]//span[text()="增强防御阈值（范围：0-10,000,000）"]/preceding-sibling::div[1]//input')
        return self.get_element_attr(ele, 'value')

    @allure.step('修改 SYN-ACK Flood 防御	增强防御阈值')
    def modify_syn_ack_enhance_pps_threshold(self, syn_ack_enhance_pps_threshold):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"SYN-ACK Flood 防御")]/../following::form[2]//span[text()="增强防御阈值（范围：0-10,000,000）"]/preceding-sibling::div[1]//input')
        ele.clear()
        ele.send_keys(syn_ack_enhance_pps_threshold)

    @allure.step('获取ACK Flood 防御 包速率限速')
    def get_ack_pps_threshold(self):
        ele = self.find_element('xpath',
                                '//h2[text()="ACK Flood 防御"]/../following::form[1]//label[text()="包速率阈值"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改SYN-ACK Flood 防御 包速率限速')
    def modify_ack_pps_threshold(self, ack_pps_threshold):
        ele = self.find_element('xpath',
                                '//h2[text()="ACK Flood 防御"]/../following::form[1]//label[text()="包速率阈值"]/following::input[1]')
        ele.clear()
        ele.send_keys(ack_pps_threshold)

    @allure.step('获取FIN/RST Flood防御 包速率阈值')
    def get_fin_rst_pps_threshold(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"FIN/RST Flood防御")]/../following::form[1]//label[text()="包速率阈值"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改FIN/RST Flood防御  包速率阈值')
    def modify_fin_rst_pps_threshold(self, ack_pps_threshold):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"FIN/RST Flood防御")]/../following::form[1]//label[text()="包速率阈值"]/following::input[1]')
        ele.clear()
        ele.send_keys(ack_pps_threshold)

    @allure.step('点击ACK Flood 防御')
    def click_ack_protection_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[text()="ACK Flood 防御"]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('点击FIN/RST Flood防御')
    def click_fin_rst_protection_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"FIN/RST Flood防御")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('点击TCP 分片攻击防御')
    def click_tcp_fragment_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"TCP 分片攻击防御")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('获取TCP 分片攻击防御 包速率阈值')
    def get_tcp_fragment_pps_threshold(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 分片攻击防御")]/../following::form[1]//label[text()="阈值"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改TCP 分片攻击防御  包速率阈值')
    def modify_tcp_fragment_pps_threshold(self, ack_pps_threshold):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 分片攻击防御")]/../following::form[1]//label[text()="阈值"]/following::input[1]')
        ele.clear()
        ele.send_keys(ack_pps_threshold)

    @allure.step('获取TCP 分片攻击防御 包速率限速')
    def get_tcp_fragment_pps_limit(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 分片攻击防御")]/../following::form[1]//label[text()="限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改TCP 分片攻击防御  包速率限速')
    def modify_tcp_fragment_pps_limit(self, ack_pps_threshold):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 分片攻击防御")]/../following::form[1]//label[text()="限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(ack_pps_threshold)

    @allure.step('点击TCP 连接耗尽攻击防御')
    def click_tcp_connect_protection_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('获取TCP 连接耗尽攻击防御 目的IP地址并发连接数阈值 ')
    def get_tcp_connect_threshold(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[1]//label[text()="目的IP地址并发连接数阈值"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改TCP 连接耗尽攻击防御 目的IP地址并发连接数阈值 ')
    def modify_tcp_connect_threshold(self, tcp_connect_threshold):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[1]//label[text()="目的IP地址并发连接数阈值"]/following::input[1]')
        ele.clear()
        ele.send_keys(tcp_connect_threshold)

    @allure.step('获取TCP 连接耗尽攻击防御 目的IP新建连接速率阈值 ')
    def get_tcp_connect_pps_threshold(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[1]//label[text()="目的IP新建连接速率阈值"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改TCP 连接耗尽攻击防御 目的IP新建连接速率阈值 ')
    def modify_tcp_connect_pps_threshold(self, tcp_connect_pps_threshold):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[1]//label[text()="目的IP新建连接速率阈值"]/following::input[1]')
        ele.clear()
        ele.send_keys(tcp_connect_pps_threshold)

    @allure.step('获取TCP 连接耗尽攻击防御 源IP并发连接限速')
    def get_src_tcp_connect_limit(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[1]//label[text()="源IP并发连接限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改TCP 连接耗尽攻击防御 源IP并发连接限速 ')
    def modify_src_tcp_connect_limit(self, src_tcp_connect_limit):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[1]//label[text()="源IP并发连接限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(src_tcp_connect_limit)

    @allure.step('获取TCP 连接耗尽攻击防御 源IP新建连接速率限速 ')
    def get_src_tcp_connect_pps_limit(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[1]//label[text()="源IP新建连接速率限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改TCP 连接耗尽攻击防御 源IP新建连接速率限速 ')
    def modify_src_tcp_connect_pps_limit(self, src_tcp_connect_pps_limit):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[1]//label[text()="源IP新建连接速率限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(src_tcp_connect_pps_limit)

    @allure.step('获取TCP 连接耗尽攻击防御 目的IP并发连接限速')
    def get_tcp_connect_pps_threshold(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[1]//label[text()="目的IP并发连接限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改TCP 连接耗尽攻击防御 目的IP并发连接限速')
    def modify_tcp_connect_pps_threshold(self, tcp_connect_pps_threshold):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[1]//label[text()="目的IP并发连接限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(tcp_connect_pps_threshold)

    @allure.step('获取TCP 连接耗尽攻击防御 目的IP新建连接速率限速')
    def get_dst_tcp_connect_pps_limit(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[1]//label[text()="目的IP新建连接速率限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改TCP 连接耗尽攻击防御 目的IP新建连接速率限速')
    def modify_dst_tcp_connect_pps_limit(self, dst_tcp_connect_pps_limit):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[1]//label[text()="目的IP新建连接速率限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(dst_tcp_connect_pps_limit)

    @allure.step('修改 源IP并发连接数异常黑名单')
    def modify_src_connect_auto_forbid_switch(self, src_connect_auto_forbid_switch):
        checked_status = False
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[2]//span[text()="源IP并发连接数异常黑名单"]/../span[1]')
        checked = self.get_element_attr(ele, 'className')
        if 'checked' in checked:
            checked_status = True
        if src_connect_auto_forbid_switch == 0 and checked_status:
            ele.click()
        if not checked_status and src_connect_auto_forbid_switch == 1:
            ele.click()

    @allure.step('修改 源IP新建连接速率异常黑名单')
    def modify_src_connect_pps_auto_forbid_switch(self, src_connect_pps_auto_forbid_switch):
        checked_status = False
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[2]//span[text()="源IP新建连接速率异常黑名单"]/../span[1]')
        checked = self.get_element_attr(ele, 'className')
        if 'checked' in checked:
            checked_status = True
        if src_connect_pps_auto_forbid_switch == 0 and checked_status:
            ele.click()
        if not checked_status and src_connect_pps_auto_forbid_switch == 1:
            ele.click()

    @allure.step('获取源IP并发连接数异常黑名单')
    def get_src_connect_auto_forbid_switch(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[2]//span[text()="源IP并发连接数异常黑名单"]/../span[1]')
        checked = self.get_element_attr(ele, 'className')
        if 'checked' in checked:
            return True
        else:
            return False

    @allure.step('获取源IP新建连接速率异常黑名单')
    def get_src_connect_pps_auto_forbid_switch(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[2]//span[text()="源IP新建连接速率异常黑名单"]/../span[1]')
        checked = self.get_element_attr(ele, 'className')
        if 'checked' in checked:
            return True
        else:
            return False

    @allure.step('获取TCP 连接耗尽攻击防御 时间')
    def get_src_connect_pps_stats_time(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[2]//span[text()="秒（范围：0-60）"]/preceding-sibling::div[1]//input')
        return self.get_element_attr(ele, 'value')

    @allure.step('修改TCP 连接耗尽攻击防御 时间')
    def modify_src_connect_pps_stats_time(self, src_syn_stats_time):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[2]//span[text()="秒（范围：0-60）"]/preceding-sibling::div[1]//input')
        ele.clear()
        ele.send_keys(src_syn_stats_time)

    @allure.step('获取TCP 连接耗尽攻击防御 连接数')
    def get_src_connect_pps_max(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[2]//span[text()="最大连接数（范围：0-1,000,000）、"]/preceding-sibling::div[1]//input')
        return self.get_element_attr(ele, 'value')

    @allure.step('修改TCP 连接耗尽攻击防御 连接数')
    def modify_src_connect_pps_max(self, src_syn_stats_time):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"TCP 连接耗尽攻击防御")]/../following::form[2]//span[text()="最大连接数（范围：0-1,000,000）、"]/preceding-sibling::div[1]//input')
        ele.clear()
        ele.send_keys(src_syn_stats_time)

    @allure.step('切换到UDP的设置')
    def switch_to_UDP(self):
        self.find_element('xpath', '//a[contains(text(),"UDP")]').click()
        result = self.verify_attr('xpath', '//a[contains(text(),"UDP")]', 'active', 'className')
        assert result ,print('没有正确转到UDP')

    @allure.step('切换到ICMP的设置')
    def switch_to_ICMP(self):
        self.find_element('xpath', '//a[contains(text(),"ICMP")]').click()
        result = self.verify_attr('xpath', '//a[contains(text(),"ICMP")]', 'active', 'className')
        assert result, print('没有正确转到')

    @allure.step('切换到DNS的设置')
    def switch_to_DNS(self):
        self.find_element('xpath', '//a[contains(text(),"DNS")]').click()
        result = self.verify_attr('xpath', '//a[contains(text(),"DNS")]', 'active', 'className')
        assert result, print('没有正确转到')

    @allure.step('切换到Other的设置')
    def switch_to_Other(self):
        self.find_element('xpath', '//a[contains(text(),"Other")]').click()
        result = self.verify_attr('xpath', '//a[contains(text(),"Other")]', 'active', 'className')
        assert result, print('没有正确转到')

    @allure.step('切换到动态黑名单的设置')
    def switch_to_black_list(self):
        self.find_element('xpath', '//a[contains(text(),"动态黑名单")]').click()
        result = self.verify_attr('xpath', '//a[contains(text(),"动态黑名单")]', 'active', 'className')
        assert result, print('没有正确转到')

    @allure.step('切换到GeoIP防护的设置')
    def switch_to_GeoIP(self):
        self.find_element('xpath', '//a[contains(text(),"GeoIP防护")]').click()
        result = self.verify_attr('xpath', '//a[contains(text(),"GeoIP防护")]', 'active', 'className')
        assert result, print('没有正确转到')

    @allure.step('切换到威胁情报的设置')
    def switch_to_threat(self):
        self.find_element('xpath', '//a[contains(text(),"威胁情报")]').click()
        result = self.verify_attr('xpath', '//a[contains(text(),"威胁情报")]', 'active', 'className')
        assert result, print('没有正确转到')

    @allure.step('切换到精准访问控制的设置')
    def switch_to_accurate(self):
        self.find_element('xpath', '//a[contains(text(),"精准访问控制")]').click()
        result = self.verify_attr('xpath', '//a[contains(text(),"精准访问控制")]', 'active', 'className')
        assert result, print('没有正确转到')


    @allure.step('返回当前udp连接阻断的状态')
    def get_drop_udp_all_switch(self):
        return self.find_element('xpath',
                                 '//h2[contains(text(),"连接阻断")]/../following-sibling::div[contains(@class,"action")]//input').text  # 值

    @allure.step('udp连接阻断')
    def click_drop_udp_all_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"连接阻断")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('返回当前icmp连接阻断的状态')
    def get_drop_icmp_all_switch(self):
        return self.find_element('xpath',
                                 '//h2[contains(text(),"连接阻断")]/../following-sibling::div[contains(@class,"action")]//input').text  # 值

    @allure.step('icmp连接阻断')
    def click_drop_icmp_all_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"连接阻断")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()


    @allure.step('UDP flood防御')
    def get_udp_protection_switch(self):
        ele = self.find_element('xpath','//h2[contains(text(),"UDP Flood 防御")]/../following-sibling::div[contains(@class,"action")]//input')
        return ele.text

    @allure.step('UDP Flood 防御 ')
    def click_udp_protection_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"UDP Flood 防御")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('获取UDP 分片攻击防御')
    def get_udp_protection_switch(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"UDP 分片攻击防御")]/../following-sibling::div[contains(@class,"action")]//input')
        return ele.text

    @allure.step('修改UDP 分片攻击防御')
    def click_udp_protection_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"UDP 分片攻击防御")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('获取UDP 分片攻击防御 阈值')
    def get_udp_fragment_pps_threshold(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"UDP 分片攻击防御")]/../following::form[1]//label[text()="阈值"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改UDP 分片攻击防御 阈值')
    def modify_udp_fragment_pps_threshold(self, udp_fragment_pps_threshold):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"UDP 分片攻击防御")]/../following::form[1]//label[text()="阈值"]/following::input[1]')
        ele.clear()
        ele.send_keys(udp_fragment_pps_threshold)

    @allure.step('获取UDP 分片攻击防御 限速')
    def get_udp_fragment_pps_limit(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"UDP 分片攻击防御")]/../following::form[1]//label[text()="限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改UDP 分片攻击防御 限速')
    def modify_udp_fragment_pps_limit(self, udp_fragment_pps_limit):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"UDP 分片攻击防御")]/../following::form[1]//label[text()="限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(udp_fragment_pps_limit)

    @allure.step('获取UDP Flood 防御 阈值')
    def get_udp_bps_threshold(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"UDP Flood 防御")]/../following::form[1]//label[text()="阈值"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改UDP Flood 防御 阈值')
    def modify_udp_bps_threshold(self, udp_bps_threshold):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"UDP Flood 防御")]/../following::form[1]//label[text()="阈值"]/following::input[1]')
        ele.clear()
        ele.send_keys(udp_bps_threshold)

    @allure.step('获取UDP Flood 防御 限速')
    def get_udp_bps_limit(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"UDP Flood 防御")]/../following::form[1]//label[text()="限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改UDP Flood 防御 限速')
    def modify_udp_bps_limit(self, udp_bps_limit):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"UDP Flood 防御")]/../following::form[1]//label[text()="限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(udp_bps_limit)

    @allure.step('获取ICMP Flood 防御 阈值')
    def get_icmp_pps_threshold(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"ICMP Flood 防御")]/../following::form[1]//label[text()="阈值"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改ICMP Flood 防御 阈值')
    def modify_icmp_bps_threshold(self, icmp_bps_threshold):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"ICMP Flood 防御")]/../following::form[1]//label[text()="阈值"]/following::input[1]')
        ele.clear()
        ele.send_keys(icmp_bps_threshold)

    @allure.step('获取ICMP Flood 防御 限速')
    def get_icmp_bps_limit(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"ICMP Flood 防御")]/../following::form[1]//label[text()="限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改ICMP Flood 防御 限速')
    def modify_icmp_bps_limit(self, icmp_bps_limit):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"ICMP Flood 防御")]/../following::form[1]//label[text()="限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(icmp_bps_limit)

    @allure.step('返回当前ICMP Flood 防御')
    def get_icmp_enhance_protection_switch(self):
        ele = self.find_element('xpath',
                                 '//h2[contains(text(),"ICMP Flood 防御")]/../following-sibling::div[contains(@class,"action")]//input')  # 值
        return self.get_element_attr(ele, 'value')

    @allure.step('ICMP Flood 防御')
    def click_icmp_enhance_protection_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"ICMP Flood 防御")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()


    @allure.step('获取 ICMP Flood 防御  ICMP 增强防御')
    def get_icmp_protection_switch(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"ICMP Flood 防御")]/../following::form[2]//span[text()="ICMP 增强防御"]/../span[1]')
        class_value = self.get_element_attr(ele, 'className')
        if 'checked' in class_value:
            return 1
        else:
            return 0

    @allure.step('修改 ICMP Flood 防御  ICMP 增强防御')
    def modify_icmp_protection_switch(self, syn_ack_port_filter_switch):
        swtich_status = False
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"ICMP Flood 防御")]/../following::form[2]//span[text()="ICMP 增强防御"]/../span[1]')
        class_value = self.get_element_attr(ele, 'className')
        if 'checked' in class_value:
            swtich_status = True
        if swtich_status and syn_ack_port_filter_switch == 0:
            ele.click()
        if not swtich_status and syn_ack_port_filter_switch == 1:
            ele.click()

    @allure.step('获取ICMP Flood 防御	时间')
    def get_src_icmp_stats_time(self):
        ele = self.find_element('xpath', '//h2[contains(text(),"ICMP Flood 防御")]/../following::form[2]//span[text()="秒（范围：0-60）"]/preceding-sibling::div[1]//input')
        return self.get_element_attr(ele, 'value')

    @allure.step('修改 ICMP Flood 防御	时间')
    def modify_src_icmp_stats_time(self, src_icmp_stats_time):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"ICMP Flood 防御")]/../following::form[2]//span[text()="秒（范围：0-60）"]/preceding-sibling::div[1]//input')
        ele.clear()
        ele.send_keys(src_icmp_stats_time)

    @allure.step('获取ICMP Flood 防御 阈值')
    def get_src_icmp_pps_min(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"ICMP Flood 防御")]/../following::form[2]//span[text()="个（阈值范围：0-1,000）"]/preceding-sibling::div[1]//input')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改ICMP Flood 防御 阈值')
    def modify_src_icmp_pps_min(self, src_icmp_pps_min):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"ICMP Flood 防御")]/../following::form[2]//span[text()="个（阈值范围：0-1,000）"]/preceding-sibling::div[1]//input')
        ele.clear()
        ele.send_keys(src_icmp_pps_min)

    #DNS
    @allure.step('返回当前DNS 防御')
    def get_dns_protection_switch(self):
        ele = self.find_element('xpath',
                                 '//h2[contains(text(),"DNS 防御")]/../following-sibling::div[contains(@class,"action")]//input')  # 值
        return self.get_element_attr(ele, 'value')

    @allure.step('DNS 防御')
    def click_dns_protection_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"DNS 防御")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('获取DNS 防御 DNS QUERY防御阈值')
    def get_dns_query_pps_threshold(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"DNS 防御")]/../following::form[1]//label[text()="DNS QUERY防御阈值"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改DNS 防御 DNS QUERY防御阈值')
    def modify_dns_query_pps_threshold(self, dns_query_pps_threshold):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"DNS 防御")]/../following::form[1]//label[text()="DNS QUERY防御阈值"]/following::input[1]')
        ele.clear()
        ele.send_keys(dns_query_pps_threshold)

    @allure.step('获取DNS QUERY 防御算法')
    def get_dns_query_protection_alg(self):
        rigth_seq = self.find_element('xpath',
                                      '//h2[contains(text(),"DNS 防御")]/../following::form[1]//label[text()="DNS QUERY 防御算法"]/following::span[contains(text(),"CNAME")]/..')
        error_seq = self.find_element('xpath',
                                      '//h2[contains(text(),"DNS 防御")]/../following::form[1]//label[text()="DNS QUERY 防御算法"]/following::span[contains(text(),"TCP")]/..')
        right_class_value = self.get_element_attr(rigth_seq, 'className')
        error_class_value = self.get_element_attr(error_seq, 'className')
        if 'checked' in right_class_value:
            return 0
        if 'checked' in error_class_value:
            return 1

    @allure.step('修改DNS QUERY 防御算法')
    def modify_dns_query_protection_alg(self, syn_protection_alg):
        rigth_seq = self.find_element('xpath',
                                      '//h2[contains(text(),"DNS 防御")]/../following::form[1]//label[text()="DNS QUERY 防御算法"]/following::span[contains(text(),"CNAME")]/..')
        error_seq = self.find_element('xpath',
                                      '//h2[contains(text(),"DNS 防御")]/../following::form[1]//label[text()="DNS QUERY 防御算法"]/following::span[contains(text(),"CNAME")]/..')
        if syn_protection_alg == 0:
            rigth_seq.click()
        else:
            error_seq.click()

    @allure.step('获取DNS 防御 DNS 源IP限速')
    def get_src_dns_query_pps_limit(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"DNS 防御")]/../following::form[2]//label[text()="DNS 源IP限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改DNS 防御 DNS 源IP限速')
    def modify_src_dns_query_pps_limit(self, src_dns_query_pps_limit):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"DNS 防御")]/../following::form[2]//label[text()="DNS 源IP限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(src_dns_query_pps_limit)

    @allure.step('获取DNS 防御 DNS 限速阈值开关')
    def get_dns_pps_limit_switch(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"DNS 防御")]/../following::form[3]//span[text()="DNS限速阈值"]/preceding-sibling::span')
        value = self.get_element_attr(ele, 'className')
        if 'checked' in value:
            return 1
        else:
            return 0

    @allure.step('修改DNS 防御 DNS 限速阈值开关')
    def modify_dns_pps_limit_switch(self, dns_pps_limit_switch):
        status = False
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"DNS 防御")]/../following::form[3]//span[text()="DNS限速阈值"]/preceding-sibling::span')
        value = self.get_element_attr(ele, 'className')
        if 'checked' in value:
            status = True
        if status and dns_pps_limit_switch == 0:
            ele.click()
        if not status and dns_pps_limit_switch == 1:
            ele.click()

    @allure.step('获取DNS 防御 DNS源IP自动封禁')
    def get_src_dns_query_auto_forbid_switch(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"DNS 防御")]/../following::form[3]//span[text()="DNS源IP自动封禁"]/preceding-sibling::span')
        value = self.get_element_attr(ele, 'className')
        if 'checked' in value:
            return 1
        else:
            return 0

    @allure.step('修改DNS 防御 DNS源IP自动封禁')
    def modify_src_dns_query_auto_forbid_switch(self, src_dns_query_auto_forbid_switch):
        status = False
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"DNS 防御")]/../following::form[3]//span[text()="DNS源IP自动封禁"]/preceding-sibling::span')
        value = self.get_element_attr(ele, 'className')
        if 'checked' in value:
            status = True
        if status and src_dns_query_auto_forbid_switch == 0:
            ele.click()
        if not status and src_dns_query_auto_forbid_switch == 1:
            ele.click()

    @allure.step('获取DNS 防御 DNS 源IP自动封禁时长')
    def get_src_dns_query_stats_time(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"DNS 防御")]/../following::form[3]//span[text()="秒（0-1000）"]/preceding-sibling::div//input')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改DNS 防御 DNS 源IP自动封禁时长')
    def modify_src_dns_query_stats_time(self, src_dns_query_stats_time):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"DNS 防御")]/../following::form[3]//span[text()="秒（0-1000）"]/preceding-sibling::div//input')
        ele.clear()
        ele.send_keys(src_dns_query_stats_time)

    @allure.step('获取DNS 防御 DNS 源IP自动封禁请求数')
    def get_src_dns_query_pps_max(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"DNS 防御")]/../following::form[3]//span[text()="最大请求数（0-1,000,000）"]/preceding-sibling::div[1]//input')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改DNS 防御 DNS 源IP自动封禁请求数')
    def modify_src_dns_query_pps_max(self, src_dns_query_pps_max):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"DNS 防御")]/../following::form[3]//span[text()="最大请求数（0-1,000,000）"]/preceding-sibling::div[1]//input')
        ele.clear()
        ele.send_keys(src_dns_query_pps_max)

    @allure.step('返回当前other连接阻断的状态')
    def get_drop_other_all_switch(self):
        return self.find_element('xpath',
                                 '//h2[contains(text(),"连接阻断")]/../following-sibling::div[contains(@class,"action")]//input').text  # 值

    @allure.step('other连接阻断')
    def click_drop_other_all_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"连接阻断")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('获取Other 防御 阈值')
    def get_other_bps_threshold(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"Other 防御")]/../following::form[1]//label[text()="阈值"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改Other 防御 阈值')
    def modify_other_bps_threshold(self, other_bps_threshold):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"Other 防御")]/../following::form[1]//label[text()="阈值"]/following::input[1]')
        ele.clear()
        ele.send_keys(other_bps_threshold)

    @allure.step('获取Other 防御 限速')
    def get_other_bps_limit(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"Other 防御")]/../following::form[1]//label[text()="限速"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改Other 防御 限速')
    def modify_other_bps_limit(self, other_bps_limit):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"Other 防御")]/../following::form[1]//label[text()="限速"]/following::input[1]')
        ele.clear()
        ele.send_keys(other_bps_limit)

    @allure.step('返回当前动态黑名单')
    def get_dynamic_black_white_list_switch(self):
        return self.find_element('xpath',
                                 '//h2[contains(text(),"超时时长")]/../following-sibling::div[contains(@class,"action")]//input').text  # 值

    @allure.step('选择动态黑名单开关')
    def click_dynamic_black_white_list_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"超时时长")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('获取动态黑名单超时时长')
    def get_src_trust_timeout(self):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"超时时长")]/../following::form[1]//label[text()="超时时长"]/following::input[1]')
        value = self.get_element_attr(ele, 'value')
        return value

    @allure.step('修改动态黑名单超时时长')
    def modify_src_trust_timeout(self, src_trust_timeout):
        ele = self.find_element('xpath',
                                '//h2[contains(text(),"超时时长")]/../following::form[1]//label[text()="超时时长"]/following::input[1]')
        ele.clear()
        ele.send_keys(src_trust_timeout)

    @allure.step('返回geoip防护')
    def get_geo_ip_filter_switch(self):
        return self.find_element('xpath',
                                 '//h2[contains(text(),"GeoIP防护")]/../following-sibling::div[contains(@class,"action")]//input').text  # 值

    @allure.step('选择geoip防护')
    def click_geo_ip_filter_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"GeoIP防护")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('返回僵尸网络IP过滤')
    def get_botip_filter_switch(self):
        ele = self.find_element('xpath',
                                 '//h2[contains(text(),"僵尸网络IP过滤")]/../following-sibling::div[contains(@class,"action")]//input') # 值
        return self.get_element_attr(ele, 'value')

    @allure.step('选择僵尸网络IP过滤')
    def click_botip_filter_switch(self, statue):
        """

        :param statue: ON / OFF 开关状态
        :return:
        """
        self.find_element('xpath',
                          '//h2[contains(text(),"僵尸网络IP过滤")]/../following-sibling::div[contains(@class,"action")]//div[contains(@class,"input")]//i').click()  # 下拉
        self.find_element('xpath',
                          '//div[not(contains(@style,"none")) and (@x-placement)]//li/span[contains(text(),"%s")]/..' % (
                              statue)).click()

    @allure.step('点击保存')
    def click_save(self):
        self.find_element('xpath','//span[text()="保存"]/..').click()
        result = self.get_success_message('操作成功')
        assert result

    @allure.step('点击新增规则')
    def click_new_rule(self):
        self.find_element('xpath','//span[text()="新增规则"]/..').click()

    @allure.step('精准访问控制')
    def fill_accurate(self, name, agreement, disposal_mode):
        result = False
        self.find_element('xpath', '//input[@placeholder="规则名称"]').send_keys(name)
        self.find_element('xpath', '//label[text()="协议"]/following-sibling::div[1]//i').click()
        self.find_element('xpath', '//div[contains(@class,"el-popper") and not(contains(@style,"none"))]//li[contains(text(),"%s")]'%agreement).click()
        self.find_element('xpath', '//label[@role="radio"]//span[text()="%s"]/preceding-sibling::span'%disposal_mode).click()
        self.find_element('xpath', '//span[text()="保存"]/..').click()
        eles = self.find_elements('xpath', '//tbody/tr/td[3]/div')
        for item in eles:
            if name == item.text:
                result = True
        assert result


