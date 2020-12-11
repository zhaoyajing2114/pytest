#web安全加速 业务列表 网站列表 首页
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from common.get_redis import get_redis_connection
from func.base import Base
import allure
from selenium import webdriver
from time import sleep
import json
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class SiteList(Base):
    @allure.step('打开web安全加速，选择模块：{1}')
    def click_web(self,module_name):
        self.find_element('xpath', '//span[text()="WEB安全加速"]/ancestor::div[contains(@class,"FeMenuItemGroup") and not(contains(@class,"header"))]',time_wait=5).click()
        sleep(1)
        self.find_element('xpath', '//span[contains(text(),"WEB安全加速")]/ancestor::div[contains(@class,"open")]//span[contains(text(),"%s")]/ancestor::a'%(module_name)).click()

    @allure.step('打开web安全加速，选择分组：{1}')
    def click_group(self, group_name):
        self.find_element("xpath",'(//input)[2]/following::i[1]',time_wait=5).click()
        sleep(2)
        self.find_element('xpath',"//li[contains(text(),'%s')]"%group_name,time_wait=10).click()
        WebDriverWait(self.driver,15,0.1).until(EC.invisibility_of_element_located((By.XPATH,'//div[contains(@class,"loading")]')))

    @allure.step('点击网站:{1}')
    def click_site(self, site_name):
        '''
        :param site_name: 网站的名称唯一定位
        :return:
        '''
        ele = self.find_element('xpath', '//a[text()="%s"]' % (site_name))  # up.lvluoyun.com
        ele.click()

    @allure.step('选择网站:{1}')
    def check_site(self,site_name):
        '''

        :param site_name: 网站的名称唯一定位
        :return:
        '''
        print(site_name)
        ele = self.find_element('xpath', '//a[text()="%s"]/preceding::input[@type="checkbox"][1]/..' % (site_name),time_wait=5)  # up.lvluoyun.com
        ele.click()

    @allure.step('点击添加网站')
    def click_add_site(self):
        self.find_element('xpath','//div[@class="DmToolbar"]/button[contains(@class,"primary")]').click()

    @allure.step('选择更多操作下的：{1}')
    def click_option(self,option_name):
        self.find_element('xpath','//span[contains(text(),"更多操作")]/i[contains(@class,"el-icon-arrow-down")]',time_wait=5).click()
        sleep(0.5)
        self.find_element('xpath','//li[contains(text(),"%s")]'%(option_name)).click()

    @allure.step('确定操作中没有：{1}')
    def verify_option_no_batch(self,option_name):
        self.find_element('xpath', '//span[contains(text(),"更多操作")]/i[contains(@class,"el-icon-arrow-down")]',time_wait=5).click()
        sleep(0.5)
        result = self.verify_element_not_exist('xpath', '//li[contains(text(),"%s")]' % (option_name))
        self.find_element('xpath', '//span[contains(text(),"更多操作")]/i[contains(@class,"el-icon-arrow-down")]',
                          time_wait=5).click()
        assert result == True,print('批量操作按钮确定不在了')

    @allure.step('确定操作中有：{1}')
    def verify_option_batch(self, option_name):
        self.find_element('xpath', '//span[contains(text(),"更多操作")]/i[contains(@class,"el-icon-arrow-down")]',
                          time_wait=5).click()
        sleep(0.5)
        result = self.verify_element_exist('xpath', '//li[contains(text(),"%s")]' % (option_name))
        self.find_element('xpath', '//span[contains(text(),"更多操作")]/i[contains(@class,"el-icon-arrow-down")]',
                          time_wait=5).click()
        assert result == True, print('有批量操作按钮')
        
    @allure.step('点击名称是{1}的修改配置')
    def click_modify(self,module_name):
        sleep(1)
        self.find_element('xpath','//div[contains(text(),"%s")]/ancestor::tr//button'%(module_name)).click()

    @allure.step('修改回源请求时长并保存:{1}')
    def modify_proxy_request_timeout(self,connect_time_out):
        ele = self.find_element('xpath', '//div[@role="dialog" and @aria-label="回源请求时长"]//input')
        ele.clear()
        ele.send_keys(connect_time_out)
        sleep(0.5)
        self.find_element('xpath', '//div[@role="dialog" and @aria-label="回源请求时长"]//span[contains(text(),"保存")]/..').click()
        # #点击继续操作
        # ele = self.find_element('xpath','//div[@aria-label="提示"]/ancestor::div[1][not(contains(@style,"none"))]//button/span[text()="继续操作"]/..',time_wait=0.2)
        # if ele != None:
        #     ele.click()
        verify_result = self.verify_element_exist('xpath', '//div[contains(@class,"el-message--success") and contains(@role,"alert")]')#操作成功字样
        assert  verify_result == True , '修改配置没有成功！'
        print('修改回源请求的操作成功')

    @allure.step('修改回源健康检查:{1}{2}{3}')
    def modify_health(self,max_fails_h,fails_timeout_h,keep_new_crc_time_h):
        ele = self.find_element('xpath', '(//div[@role="dialog" and @aria-label="回源健康检查"]//input)[1]')#回源失败次数
        ele.clear()
        ele.send_keys(max_fails_h)
        sleep(0.5)
        ele = self.find_element('xpath', '(//div[@role="dialog" and @aria-label="回源健康检查"]//input)[2]')  # 回源失败统计时间间隔
        ele.clear()
        ele.send_keys(fails_timeout_h)
        sleep(0.5)
        ele = self.find_element('xpath', '(//div[@role="dialog" and @aria-label="回源健康检查"]//input)[3]')  # 回源失败禁用不可用IP时间
        ele.clear()
        ele.send_keys(keep_new_crc_time_h)
        sleep(0.5)
        self.find_element('xpath','//div[@role="dialog" and @aria-label="回源健康检查"]//span[contains(text(),"保存")]/..').click()
        # ele=self.find_element('xpath','//div[@aria-label="提示"]/ancestor::div[1][not(contains(@style,"none"))]//button/span[text()="继续操作"]/..')
        # if ele != None:
        #     ele.click()
        verify_result = self.verify_element_exist('xpath','//div[contains(@class,"success") and contains(@class,"message")]')  # 操作成功字样
        assert verify_result == True, '修改配置没有成功！'
        print('修改回源请求的操作成功')

    @allure.step('修改回源保持长链接')
    def modify_keepalive(self,status):
        self.find_element('xpath', '//div[@role="dialog" and @aria-label="回源保持长连接"]//span[@class="el-input__suffix"]').click()
        sleep(0.5)
        self.find_element('xpath', '//li[contains(text(),"%s")]'%(status)).click()
        self.verify_attr('xpath','//div[@role="dialog" and @aria-label="回源保持长连接"]//input',status,'value')
        self.find_element('xpath',
                          '//div[@role="dialog" and @aria-label="回源保持长连接"]//span[contains(text(),"保存")]/..').click()
        # 点击继续操作
        # ele = self.find_element('xpath',
        #                         '//div[@aria-label="提示"]/ancestor::div[1][not(contains(@style,"none"))]//button/span[text()="继续操作"]/..')
        # if ele != None:
        #     ele.click()
        verify_result = self.verify_element_exist('xpath',
                                                  '//div[contains(@class,"success") and contains(@class,"message")]')  # 操作成功字样
        assert verify_result == True, '修改配置没有成功！'
        print('修改回源保持长连接的操作成功')

    @allure.step('修改https')
    def modify_https(self,second_time):
        '''

        :param except_cert_list: 预期的下拉列表中的值
        :param choose_cert: 选择的证书
        :return:
        '''
        sleep(2)
        self.find_element('xpath','//div[contains(text(),"提供 SSL 服务") and contains(@class,"body")]/following::i[1]').click()#选择证书的下拉框
        #校验下拉列表中的证书
        if second_time == 1:
            self.find_element('xpath','//div[contains(@class,"el-popper") and contains(@x-placement,"bottom-start")]//ul/li[contains(text(),"OFF")]',time_wait=5).click()#选择停用
            result_off = self.verify_attr('xpath','//form[contains(@class,"left")]','display','style')
            assert  result_off == True ,print('OFF的情况下不允许修改其他值')
        else:
            sleep(0.5)
            self.find_element('xpath','//div[contains(@class,"el-popper") and contains(@x-placement,"bottom-start")]//ul/li[contains(text(),"ON")]').click()  # 选择证书 默认选择一个
            self.find_element('xpath', '//label[text()="选择证书"]/following::i[1]').click()
            self.find_element('xpath', '//div[contains(@class,"el-popper") and contains(@x-placement,"bottom-start")]//ul/li[3]').click()
            self.find_element('xpath','//span[text()="全量跳转"]/preceding::input[1]/../span').click()#点击全量跳转
            self.find_element('xpath', '//label[text()="HTTP2"]/following::input[2]/../span').click()#http2选择ON
            self.find_element('xpath','//label[text()="HSTS"]/following::input[2]/../span').click()#hsts选ON
            self.find_element('xpath','//label[text()="支持的最小TLS版本"]/following::i[1]').click()#支持的TLS版本下拉
            sleep(0.5)
            self.find_element('xpath','//ul[contains(@class,"dropdown")]/li[contains(text(),"TLSv1.2")]').click()#选择tls1.2
            result_choose = self.verify_attr('xpath', '//label[text()="支持的最小TLS版本"]/following::input', 'TLSv1.2', 'value')
            assert result_choose == True ,print('当前接口的tls版本错误')
            self.find_element('xpath',
                              '//div[@role="dialog" and @aria-label="HTTPS"]//span[contains(text(),"保存")]/..').click()
            # 点击继续操作
            # ele = self.find_element('xpath',
            #                         '//div[@aria-label="提示"]/ancestor::div[1][not(contains(@style,"none"))]//button/span[text()="继续操作"]/..')
            # if ele != None:
            #     ele.click()
            verify_result = self.verify_element_exist('xpath',
                                                      '//div[contains(@class,"success") and contains(@class,"message")]')  # 操作成功字样
            assert verify_result == True, '修改配置没有成功！'
            print('修改https的操作成功')

    @allure.step('点击删除')
    def click_delete_site(self):
        assert self.verify_element_not_exist('css','.ya-phone-fill',3) == True#登录提示


    @allure.step('从redis中获取网站的初始配置')
    def get_formal_config_in_redis(self,site_name,except_result):
        '''

        :param site_name: 网站的名称
        :param except_result: 期望从redis中获取到的配置项list
        :return:返回字典 配置项内容和redis中存放的结果
        '''
        redis_conn = get_redis_connection()
        try:
            a = redis_conn.get(site_name)
            redis_result = json.loads(a)
            result_dict = {}
            for item in except_result:
                if '.' in item:
                    a = item.split('.')
                    try:
                        result_dict.update({item:redis_result[a[0]][a[1]]})
                    except:
                        result_dict.update({item:'none'})
                else:
                    result_dict.update({item:redis_result[item]})
            print(result_dict)
            return result_dict
        except BaseException as e:
            print(str(e))

    @allure.step('校验网站的配置和预期是否一致')
    def verify_config(self,group_name,site_name):
        #校验网页上展示的内容和redis中胡哦去到的内容是否一致
        '''
        :param site_name: 网站名称
        :return:
        '''
        redis_conn = get_redis_connection()  # 获取redis链接
        try:
            a = redis_conn.get(site_name)
            redis_result = json.loads(a)
        except BaseException as e:
            print(str(e))
        try:
            self.click_group(group_name)
            #进入网站
            site_path = '//a[text()="' + site_name + '"]'
            locator = (By.XPATH, site_path)
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
            self.find_element('xpath',site_path).click()  # 点击网站的域名
            # 获取网站的配置
            # 1.获取源站设置
            locator = (By.XPATH, '//h2[contains(text(),"源站设置")]')#等待源站设置
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
            row_num = len(self.find_elements('xpath','//h2[text()="源站设置"]/../../div[2]//table[contains(@class,"body")]//tr'))
            # col_num = len(self.find_elements('xpath',
            #     '//h2[text()="源站设置"]/../../div[2]//table[contains(@class,"body")]//tr[1]/td'))
            for i in range(0, row_num):
                portcfg = self.find_element('xpath',
                    '//h2[text()="源站设置"]/../../div[2]//table[contains(@class,"body")]//tr[%s]/td[1]//div[@class="cell"]' % (
                            i + 1)).text
                listen_port = self.find_element('xpath',
                    '//h2[text()="源站设置"]/../../div[2]//table[contains(@class,"body")]//tr[%s]/td[2]//div[@class="cell"]' % (
                            i + 1)).text
                proxy_protocol = self.find_element('xpath',
                    '//h2[text()="源站设置"]/../../div[2]//table[contains(@class,"body")]//tr[%s]/td[3]//div[@class="cell"]' % (
                            i + 1)).text
                ip_port = self.find_element('xpath',
                    '//h2[text()="源站设置"]/../../div[2]//table[contains(@class,"body")]//tr[%s]/td[4]//div[@class="cell"]' % (
                            i + 1)).text
                print('第%s行数据：协议类型：%s  取源端口：%s  取源协议：%s  源站地址：%s' % (i, portcfg, listen_port, proxy_protocol, ip_port))
                try:
                    temp = redis_result['portcfg'][listen_port]
                    if temp['proxy_protocol'] != proxy_protocol.lower():
                        print('协议类型不存在！')
                    if temp['upstream']['any'][0]['ip'] != ip_port:
                        print('源站地址不正确！')
                except BaseException as e:
                    print(str(e))
                    print('端口不存在：%s' % listen_port)
            #获取回源host是否打开
            proxy_host = self.find_element('xpath','//h2[text()="回源 HOST"]/../../div[3]//input')
            print(self.driver.execute_script('return arguments[0].value', proxy_host))
            # 如果是默认 则redis中没有配置，如果有host--proxy_host
            #获取range回源
            range1 = self.find_element('xpath','//h2[text()="Range 回源"]/../../div[3]//input')
            print(self.driver.execute_script('return arguments[0].value', range1))
            #获取回源请求时长
            proxy_connect_timeout = self.find_element('xpath','//h2[text()="回源请求时长"]/../../div[2]//input')
            proxy_connect_timeout = self.driver.execute_script('return arguments[0].value', proxy_connect_timeout)
            try:
                assert str(redis_result['proxy_connect_timeout']) != proxy_connect_timeout ,print('回源请求时长不一致%s--%s' % (proxy_connect_timeout, redis_result['proxy_connect_timeout']))
            except BaseException as e:
                print(str(e))
                print('proxy_connect_timeout字段不存在')
            #获取回源保持长连接是否开启
            proxy_keepalive = self.find_element('xpath','//h2[text()="回源保持长连接"]/../../div[3]//input')
            proxy_keepalive = self.driver.execute_script('return arguments[0].value', proxy_keepalive)
            if proxy_keepalive == 'OFF':
                proxy_keepalive = 0
            else:
                proxy_keepalive = 1
            try:
                assert redis_result['proxy_keepalive'] != proxy_keepalive,print('回源保持长链接不一致%s--%s' % (proxy_keepalive, redis_result['proxy_keepalive']))
            except BaseException as e:
                print(str(e))
                print('proxy_keepalive字段不存在')
            #获取回源健康检查 设置
            max_fails = self.find_element('xpath','//label[text()="回源失败次数"]/following::input[1]')
            max_fails = self.driver.execute_script('return arguments[0].value', max_fails)
            fails_timeout = self.find_element('xpath','//label[text()="回源失败统计时间间隔"]/following::input[1]')
            fails_timeout = self.driver.execute_script('return arguments[0].value', fails_timeout)
            keep_new_src_time = self.find_element('xpath','//label[text()="回源失败禁用不可用IP时间"]/following::input[1]')
            keep_new_src_time = self.driver.execute_script('return arguments[0].value', keep_new_src_time)
            try:
                check = redis_result['health_check']
                assert check['max_fails'] != int(max_fails), print('回源失败次数%s--%s' % (max_fails, check['max_fails']))
                assert check['fails_timeout'] != int(fails_timeout),print('回源失败统计时间间隔%s--%s' % (fails_timeout, check['fails_timeout']))
                assert check['keep_new_src_time'] != int(keep_new_src_time), print('回源失败禁用不可用IP时间%s--%s' % (keep_new_src_time, check['keep_new_src_time']))
            except BaseException as e:
                print(str(e))
                print('health_check字段不存在')
            # 换页 进入高级配置页面
            self.find_element('xpath','//a[contains(text(),"高级配置")]').click()
            sleep(0.5)
            #获取https相关的信息
            https = self.find_element('xpath','//h2[text()="HTTPS"]/../../div[3]//input')
            https = self.driver.execute_script('return arguments[0].value', https)
            if https == 'OFF':
                try:
                    if redis_result['ssl']:
                        print('不应该存在ssl字段，因为https关闭')
                except:
                    print('确实不存在ssl字段，正确')
            else:
                http2https = self.find_element('xpath',
                    '//label[contains(text(),"HTTP 跳转 HTTPS")]/following::span[contains(@class,"is-checked")]//input')\
                    .get_attribute('value')
                if 'all' in http2https:
                    http2https = 1
                elif 'off' in http2https:
                    http2https = 0
                elif 'special' in http2https:
                    http2https = 2
                else:
                    http2https = -1
                    print('没有选中的！')
                http2_disable = self.find_element('xpath',
                    '//label[contains(text(),"HTTP2")]/following::div[1]/div[1]').get_attribute('class')
                if 'is-checked' in http2_disable:
                    http2_disable = 0
                else:
                    http2_disable = 1
                HSTS = self.find_element('xpath',
                    '//label[contains(text(),"HSTS")]/following::div[1]/div[1]').get_attribute('class')
                if 'is-checked' in HSTS:
                    HSTS = 1
                else:
                    HSTS = 0
                min_version = self.find_element('xpath','//label[contains(text(),"支持的最小TLS版本")]/following::input[1]')
                min_version = self.driver.execute_script('return arguments[0].value', min_version)
                try:
                    check = redis_result['ssl']
                    assert check['http2https'] != http2https,print('HTTP 跳转 HTTPS%s--%s' % (http2https, check['http2https']))
                    assert check['http2_disable'] != http2_disable, print('HTTP2  %s--%s' % (http2_disable, check['http2_disable']))
                    assert check['hsts'] != HSTS, print('回源失败禁用不可用IP时间%s--%s' % (HSTS, check['HSTS']))
                    assert min_version not in check['min_version'],print('TLS版本与redis中的不一致！%s----%s' % (min_version, check['min_version']))
                except BaseException as e:
                    print(str(e))
                    print('ssl字段不存在')

        except BaseException as e:
            print(str(e))
        finally:
            # 返回之前页面
            self.find_element('xpath','//i[contains(@class,"el-icon-back")]/..',time_wait=5).click()

    @allure.step('校验体验版没有tls版本和回源健康检查按钮,并且redis中没有回源健康检查')
    def verify_experience_edition(self):
        first_ele = self.find_element('xpath','//div[contains(@class,"DmData-table")]//tr[1]/td[2]//a')
        site_name_temp = first_ele.text
        first_ele.click()
        self.find_element('xpath','//h2[text()="回源请求时长"]/../../div[2]//input',time_wait=10)
        result = self.verify_element_not_exist('xpath','//label[text()="回源失败次数"]/following::input[1]')
        assert result == True, print('界面上还存在回源健康检查')
        # 换页 进入高级配置页面
        self.find_element('xpath', '//a[contains(text(),"高级配置")]').click()
        sleep(0.5)
        result = self.verify_element_not_exist('xpath','//label[contains(text(),"支持的最小TLS版本")]/following::input[1]')
        assert result == True , print('界面上还存在TLS版本')
        redis_conn = get_redis_connection()  # 获取redis链接
        try:
            a = redis_conn.get(site_name_temp)
            redis_result = json.loads(a)
        except BaseException as e:
            print(str(e))
        print(123)
        if 'health_check' not in redis_result.keys():
            print('redis中正常的没有回源健康检查！')
        else:
            assert False

    @allure.step('校验高级版有tls版本和回源健康检查按钮，并且redis中有回源健康检查')
    def verify_high_edition(self):
        first_ele = self.find_element('xpath', '//div[contains(@class,"DmData-table")]//tr[1]/td[2]//a')
        site_name_temp = first_ele.text
        first_ele.click()
        self.find_element('xpath', '//h2[text()="回源请求时长"]/../../div[2]//input', time_wait=10)
        result = self.verify_element_exist('xpath', '//label[text()="回源失败次数"]/following::input[1]')
        assert result == True, print('界面上不存在回源健康检查')
        # 换页 进入高级配置页面
        self.find_element('xpath', '//a[contains(text(),"高级配置")]').click()
        sleep(0.5)
        result = self.verify_element_exist('xpath', '//label[contains(text(),"支持的最小TLS版本")]/following::input[1]')
        assert result == True, print('界面上不存在TLS版本')
        redis_conn = get_redis_connection()  # 获取redis链接
        try:
            a = redis_conn.get(site_name_temp)
            redis_result = json.loads(a)
        except BaseException as e:
            print(str(e))
        print(123)
        if 'health_check' in redis_result.keys():
            print('redis中正常有回源健康检查！')
        else:
            assert False