import sys
import os
import allure
import pytest
from time import sleep
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())
print(sys.path)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.page
@allure.feature('测试修改配置并校验配置是否生效')
class TestConfig:
    @pytest.mark.test
    @pytest.mark.run(order=1)
    @allure.story('登录')
    @allure.description('登录')
    def test_login(self,browser):
        driver = browser[0]
        url = browser[2]['url']
        username = browser[2]['username']
        password = browser[2]['password']
        success_sign = browser[2]['success_sign']
        login_success = False
        try_time = 3
        while not login_success and try_time > 0:
            try:
                driver.get(url + '/login')
                driver.find_element_by_id('username').send_keys(username)
                driver.find_element_by_id('password').send_keys(password)
                driver.find_element_by_xpath('//button[@type="submit"]').click()
                sleep(2)
                WebDriverWait(driver, 5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, success_sign)))
                login_success = True
            except:
                login_success = False
                try_time = try_time - 1
        assert login_success == True,'登陆失败'

    @allure.story('批量修改回源请求时长-验证批量修改生效并且其他的参数不受影响')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("connect_time_out",[55,66])
    @allure.description('批量修改回源请求时长，改两次')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_proxy_connect_timeout(self,connect_time_out,browser):
        site_list_page = browser[1]['web安全加速']
        page = browser[1]['登录页面']
        env = browser[2]
        except_result = ['config_time', 'server_name', 'ssl.status', 'ssl.http2https', 'ssl.min_version',
                         'ssl.http2_disable'
            , 'ssl.hsts', 'proxy_connect_timeout', 'proxy_keepalive', 'health_check.max_fails',
                         'health_check.fails_timeout', 'health_check.keep_new_src_time']
        with allure.step('获取网站的初始配置'):
            before_conf_list = []#被测网址的配置
            # site_names = ['1014.lvluoyun.com','0922.lvluoyun.com','www.lvluoyun.com']
            site_names = env['site_names']
            for item in site_names:
                before_config = site_list_page.get_formal_config_in_redis(item,except_result)
                before_conf_list.append(before_config)
        with allure.step('打开web安全加速，进行分组筛选，批量选择网站'):
            site_list_page.click_web('业务列表')
            #进行分组筛选
            site_list_page.click_group('自动化测试使用')
            for item in site_names:
                site_list_page.check_site(item)
            site_list_page.click_option('批量配置')
        with allure.step('修改回源请求时长为%s并保存'%connect_time_out):
            site_list_page.click_modify('回源请求时长')
            site_list_page.modify_proxy_request_timeout(connect_time_out)
        k = len(site_names)
        with allure.step('获取网站修改之后的配置'):
            page.open('%s/console/cloud-speed/businessList/websiteList'%env['url'])
            after_config_list = []
            for i in range(0,k):
                site_list_page.verify_config(group_name='自动化测试使用',site_name=site_names[i])
                after_conf = site_list_page.get_formal_config_in_redis(site_names[i],except_result)
                after_config_list.append(after_conf)
        response = ''
        for i in range(0,k):
            a = before_conf_list[i]
            b = after_config_list[i]
            with allure.step('比对前后数据'):
                title = ''
                line1 = ''
                line2 = ''
                for item in except_result:
                    title = title + str(item).replace(",", "，") + ","
                    line1 = line1 + str(a[item]).replace(",", "，") + ","
                    line2 = line2 + str(b[item]).replace(',','，') + ','
                    response = title +"\n" + line1 +"\n" + line2 +"\n"
                allure.attach(response, "前后结果", allure.attachment_type.CSV)
                for item in except_result:
                    if item == 'proxy_connect_timeout':
                        assert b['proxy_connect_timeout'] == connect_time_out,print('回源请求时长正常是%s'%(connect_time_out))
                    elif item == 'config_time':
                        print('获取时间，不进行比对')
                    else:
                        assert a[item] == b[item] ,print('修改前后%s字段不一致'%item)

    @allure.story('批量修改回源健康检查-验证批量修改生效并且其他的参数不受影响')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("max_fails_h,fails_timeout_h,keep_new_crc_time_h", [(100,99,123), (23,23,23)])
    def test_health(self,max_fails_h,fails_timeout_h,keep_new_crc_time_h,browser):
        site_list_page = browser[1]['web安全加速']
        page = browser[1]['登录页面']
        env = browser[2]
        except_result = ['config_time', 'server_name', 'ssl.status', 'ssl.http2https', 'ssl.min_version',
                         'ssl.http2_disable'
            , 'ssl.hsts', 'proxy_connect_timeout', 'proxy_keepalive', 'health_check.max_fails',
                         'health_check.fails_timeout', 'health_check.keep_new_src_time']
        with allure.step('获取网站的初始配置'):
            before_conf_list = []#被测网址的配置
            #site_names = ['1014.lvluoyun.com','0922.lvluoyun.com','www.lvluoyun.com']
            site_names = env['site_names']
            for item in site_names:
                before_config = site_list_page.get_formal_config_in_redis(item,except_result)
                before_conf_list.append(before_config)
        k = len(site_names)
        with allure.step('打开web安全加速，批量选择网站'):
            site_list_page.click_web('业务列表')
            # 进行分组筛选
            site_list_page.click_group('自动化测试使用')
            for item in site_names:
                site_list_page.check_site(item)
            site_list_page.click_option('批量配置')
        with allure.step('修改回源健康检查'):
            allure.attach('健康检查修改情况','回源失败次数，%s\n回源失败统计时间间隔，%s\n回源失败禁用不可用IP时间，%s\n'%(max_fails_h,fails_timeout_h,keep_new_crc_time_h),allure.attachment_type.CSV)
            site_list_page.click_modify('回源健康检查')
            site_list_page.modify_health(max_fails_h,fails_timeout_h,keep_new_crc_time_h)
        with allure.step('获取网站修改之后的配置'):
            page.open('%s/console/cloud-speed/businessList/websiteList'%env['url'])
            after_config_list = []
            for i in range(0,k):
                site_list_page.verify_config(group_name='自动化测试使用',site_name=site_names[i])
                after_conf = site_list_page.get_formal_config_in_redis(site_names[i],except_result)
                after_config_list.append(after_conf)
        response = ''
        for i in range(0,k):
            a = before_conf_list[i]
            b = after_config_list[i]
            with allure.step('比对前后数据'):
                title = ''
                line1 = ''
                line2 = ''
                for item in except_result:
                    title = title + str(item).replace(",", "，") + ","
                    line1 = line1 + str(a[item]).replace(",", "，") + ","
                    line2 = line2 + str(b[item]).replace(',','，') + ','
                    response = title +"\n" + line1 +"\n" + line2 +"\n"
                allure.attach(response, "前后结果", allure.attachment_type.CSV)
                for item in except_result:
                    if item == 'health_check.max_fails':
                        assert b['health_check.max_fails'] == max_fails_h,print('回源失败次数，100')
                    elif item == 'health_check.fails_timeout':
                        assert b['health_check.fails_timeout'] == fails_timeout_h,print('回源失败统计时间间隔，999')
                    elif item == 'health_check.keep_new_src_time':
                        assert b['health_check.keep_new_src_time'] == keep_new_crc_time_h,print('回源失败禁用不可用IP时间，45')
                    elif item == 'config_time':
                        print('获取时间，不进行比对')
                    else:
                        assert a[item] == b[item] ,print('修改前后%s字段不一致'%item)

    @allure.story('批量修改回源保持长连接-验证批量修改生效并且其他的参数不受影响')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('status',['开启','关闭'])
    def test_proxy_keepalive(self,status,browser):
        site_list_page = browser[1]['web安全加速']
        page = browser[1]['登录页面']
        env = browser[2]
        except_result = ['config_time', 'server_name', 'ssl.status', 'ssl.http2https', 'ssl.min_version',
                         'ssl.http2_disable'
            , 'ssl.hsts', 'proxy_connect_timeout', 'proxy_keepalive', 'health_check.max_fails',
                         'health_check.fails_timeout', 'health_check.keep_new_src_time']
        with allure.step('获取网站的初始配置'):
            before_conf_list = []#被测网址的配置
            # site_names = ['1014.lvluoyun.com','0922.lvluoyun.com','www.lvluoyun.com']
            site_names = env['site_names']
            for item in site_names:
                before_config = site_list_page.get_formal_config_in_redis(item,except_result)
                before_conf_list.append(before_config)
        k = len(site_names)
        with allure.step('打开web安全加速，批量选择网站'):
            site_list_page.click_web('业务列表')
            # 进行分组筛选
            site_list_page.click_group('自动化测试使用')
            for item in site_names:
                site_list_page.check_site(item)
            site_list_page.click_option('批量配置')
        with allure.step('修改回源保持长连接'):
            allure.attach('回源保持长连接修改情况','回源保持长连接,打开',allure.attachment_type.CSV)
            site_list_page.click_modify('回源保持长连接')
            site_list_page.modify_keepalive(status)
        print('123')
        with allure.step('获取网站修改之后的配置'):
            page.open('%s/console/cloud-speed/businessList/websiteList'%(env['url']))
            after_config_list = []
            for i in range(0,k):
                site_list_page.verify_config(group_name='自动化测试使用',site_name=site_names[i])
                after_conf = site_list_page.get_formal_config_in_redis(site_names[i],except_result)
                after_config_list.append(after_conf)
        response = ''
        for i in range(0,k):
            a = before_conf_list[i]
            b = after_config_list[i]
            with allure.step('比对前后数据'):
                title = ''
                line1 = ''
                line2 = ''
                for item in except_result:
                    title = title + str(item).replace(",", "，") + ","
                    line1 = line1 + str(a[item]).replace(",", "，") + ","
                    line2 = line2 + str(b[item]).replace(',','，') + ','
                    response = title +"\n" + line1 +"\n" + line2 +"\n"
                allure.attach(response, "前后结果", allure.attachment_type.CSV)
                for item in except_result:
                    if item == 'proxy_keepalive':
                        if status == '开启':
                            res = 1
                        else:
                            res = 0
                        assert b['proxy_keepalive'] == res,print('回源保持长连接')
                    elif item == 'config_time':
                        print('获取时间，不进行比对')
                    else:
                        assert a[item] == b[item] ,print('修改前后%s字段不一致'%item)


    @pytest.mark.test
    @allure.story('批量修改tls版本')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('second_time', [0, 1])
    def test_https_default(self, second_time,browser):
        site_list_page = browser[1]['web安全加速']
        page = browser[1]['登录页面']
        env = browser[2]
        except_result = ['config_time', 'server_name', 'ssl.status', 'ssl.key', 'ssl.http2https', 'ssl.min_version',
                         'ssl.http2_disable'
            , 'ssl.hsts', 'proxy_connect_timeout', 'proxy_keepalive', 'health_check.max_fails',
                         'health_check.fails_timeout', 'health_check.keep_new_src_time']
        with allure.step('获取网站的初始配置'):
            before_conf_list = []  # 被测网址的配置
            # site_names = ['1014.lvluoyun.com','0922.lvluoyun.com','www.lvluoyun.com']
            site_names = env['site_names']
            for item in site_names:
                before_config = site_list_page.get_formal_config_in_redis(item, except_result)
                before_conf_list.append(before_config)
        with allure.step('打开web安全加速，批量选择网站'):
            site_list_page.refresh()
            sleep(2)
            site_list_page.click_web('业务列表')
            sleep(3)
            # 进行分组筛选
            site_list_page.click_group('自动化测试使用')
            for item in site_names:
                site_list_page.check_site(item)
            site_list_page.click_option('批量配置')
        with allure.step('进行https的配置'):
            allure.attach( 'HTTP 跳转 HTTPS:全量跳转\nHTTP2：on\nHSTS:on\n支持的TLS版本:TLS1.2','高级配置项https修改内容' ,allure.attachment_type.CSV)
            site_list_page.click_modify('HTTPS')
            # 证书列表中的标志证书的值
            # www.lvluoyun.com中的结束字符串是Fuw13kt9i+e8=
            # *.lvluoyun.com中的开始字符串是9X7suvuVa5Xg=
            # 证书字典--
            site_list_page.modify_https(second_time)
        print('123')
        k = len(site_names)
        with allure.step('获取网站修改之后的配置'):
            page.open('%s/console/cloud-speed/businessList/websiteList' % env['url'])
            after_config_list = []
            for i in range(0, k):
                site_list_page.verify_config(group_name='自动化测试使用',site_name=site_names[i])
                after_conf = site_list_page.get_formal_config_in_redis(site_names[i], except_result)
                after_config_list.append(after_conf)
        response = ''
        for i in range(0, k):
            a = before_conf_list[i]
            b = after_config_list[i]
            with allure.step('比对前后数据'):
                title = ''
                line1 = ''
                line2 = ''
                for item in except_result:
                    title = title + str(item).replace(",", "，") + ","
                    if item == 'ssl.key':
                        line1 = line1 + str(a[item].split('=')[0][-12:]).replace(",", "，") + ","
                        line2 = line2 + str(b[item].split('=')[0][-12:]).replace(',', '，') + ','
                    else:
                        line1 = line1 + str(a[item]).replace(",", "，") + ","
                        line2 = line2 + str(b[item]).replace(',', '，') + ','
                    response = title + "\n" + line1 + "\n" + line2 + "\n"
                allure.attach(response, "前后结果", allure.attachment_type.CSV)
                for item in except_result:
                    if item == 'ssl.status':
                        assert b['ssl.status'] == 1, print('ssl状态是开启')
                    elif item == 'ssl.http2https':
                        assert b[item] == 1
                    elif item == 'ssl.min_version':
                        assert b[item] == 'TLSv1.2'
                    elif item == 'ssl.http2_disable':  # 这里是反的
                        assert b[item] == 0
                    elif item == 'ssl.hsts':
                        assert b[item] == 1
                    elif item == 'config_time':
                        print('获取时间，不进行比对')
                    elif item == 'ssl.key':
                        key_value = b[item].split('=')[0][-12:]
                        assert key_value != None, print('当前证书的值错误')
                    else:
                        assert a[item] == b[item], print('修改前后%s字段不一致' % item)

    @allure.story('降低套餐版本')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=6)
    def test_reduce_version(self,browser):
        site_list_page = browser[1]['web安全加速']
        page = browser[1]['登录页面']
        v6page = browser[1]['订单管理系统']
        env = browser[2]
        with allure.step('登录订单管理系统'):
            url = env['v6_url']
            nm = env['v6_username']
            pwd = env['v6_password']
            v6page.login_adminv6(url,nm,pwd)
        with allure.step('进入订单管理系统-调整套餐版本-退订'):
            v6page.choose_menu()
            v6page.search_mail('1208010487@qq.com')
            v6page.cancel()
        with allure.step('验证退订套餐之后的 回源健康检查和tls版本批量操作消失'):
            page.open(env['url']+'/console/home')#返回 控制台
            site_list_page.click_web('业务列表')
            site_list_page.verify_text('xpath',
                                            '//div[contains(text(),"当前套餐版本")]//button[contains(@class,"popover")]/span',
                                            '体验版')
            # 进行分组筛选
            site_names = env['site_names']
            site_list_page.click_group('自动化测试使用')
            for item in site_names:
                site_list_page.check_site(item)
            site_list_page.verify_option_no_batch('批量配置')#校验批量操作的按钮已经没有了
            site_list_page.verify_experience_edition()



    @allure.story('升高套餐版本')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=7)
    def test_upgrade_version(self,browser):
        site_list_page = browser[1]['web安全加速']
        page = browser[1]['登录页面']
        v6page = browser[1]['订单管理系统']
        env = browser[2]
        #自动判断是否已经登录成功了
        with allure.step('登录订单管理系统'):
            url = env['v6_url']
            nm = env['v6_username']
            pwd = env['v6_password']
            v6page.login_adminv6(url, nm, pwd)
        with allure.step('进入订单管理系统-重新订购新的套餐'):
            v6page.choose_menu()
            v6page.search_mail('1208010487@qq.com')
            v6page.upgrade('1208010487@qq.com')
        with allure.step('验证回源健康检查和tls版本回源之后会重新显示并恢复默认值'):
            page.open(env['url'] + '/console/home')  # 返回 控制台
            site_list_page.click_web('业务列表')
            site_list_page.verify_text('xpath', '//div[contains(text(),"当前套餐版本")]//button[contains(@class,"popover")]/span','高级版')
            # 进行分组筛选
            site_names = env['site_names']
            site_list_page.click_group('自动化测试使用')
            for item in site_names:
                site_list_page.check_site(item)
            site_list_page.verify_option_batch('批量配置')  # 校验批量操作的按钮已经没有了
            site_list_page.verify_high_edition()

