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
from copy import deepcopy

@allure.feature('ddos页面的测试')
class Test_Ddos:

    @pytest.mark.run(order=1)
    @allure.story('登录')
    @pytest.mark.login
    # @pytest.mark.test
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
        assert login_success == True, '登陆失败'

    @pytest.mark.run(order=2)
    @allure.story('批量删除所有的集群')
    #@pytest.mark.skip
    def test_delete_bag_grabbing_list(self, browser):
        ddos_list = browser[1]['ddos任务列表']
        ddos_cluster_page = browser[1]['ddos集群管理']
        ddos_cluster_page.refresh()
        ddos_list.click_menu('抓包工具')
        sleep(1)
        flag = not ddos_cluster_page.verify_element_exist('xpath', '//span[text()="暂无数据"]',time_wait=4)
        while flag:
            ddos_cluster_page.click_all()
            ddos_cluster_page.click_delete()
            with allure.step('验证删除成功'):
                msg = ddos_cluster_page.get_success_message('成功')
                assert msg, '删除失败'
            flag = not ddos_cluster_page.verify_element_exist('xpath', '//span[text()="暂无数据"]',time_wait=4)

    @pytest.mark.run(order=3)
    @allure.story('批量删除所有的防御域')
    #@pytest.mark.skip
    def test_delete_defence_group(self, browser):
        ddos_list = browser[1]['ddos任务列表']
        ddos_cluster_page = browser[1]['ddos集群管理']
        ddos_cluster_page.refresh()
        ddos_list.click_menu('业务列表')
        sleep(1)
        flag = not ddos_cluster_page.verify_element_exist('xpath', '//span[text()="暂无数据"]', time_wait=4)
        while flag:
            ddos_cluster_page.click_all()
            ddos_cluster_page.click_delete()
            with allure.step('验证删除成功'):
                msg = ddos_cluster_page.get_success_message('操作成功')
                assert msg, '删除失败'
            flag = not ddos_cluster_page.verify_element_exist('xpath', '//span[text()="暂无数据"]', time_wait=4)

    @pytest.mark.run(order=4)
    @allure.story('批量删除所有的集群')
    #@pytest.mark.skip
    def test_delete_cluster(self,browser):
        ddos_list = browser[1]['ddos任务列表']
        ddos_cluster_page = browser[1]['ddos集群管理']
        ddos_cluster_page.refresh()
        ddos_list.click_menu('集群管理')
        sleep(3)
        flag = not ddos_cluster_page.verify_element_exist('xpath', '//span[text()="暂无数据"]', time_wait=4)
        while flag:
            ddos_cluster_page.click_all()
            ddos_cluster_page.click_delete()
            with allure.step('验证删除成功'):
                msg = ddos_cluster_page.get_success_message('成功')
                assert msg, '删除失败'
            flag = not ddos_cluster_page.verify_element_exist('xpath', '//span[text()="暂无数据"]', time_wait=4)

    @pytest.mark.run(order=5)
    @allure.story('批量删除所有的配置模板')
    #@pytest.mark.skip
    def test_delete_model(self, browser):
        ddos_list = browser[1]['ddos任务列表']
        ddos_cluster_page = browser[1]['ddos集群管理']
        ddos_cluster_page.refresh()
        ddos_list.click_menu('配置模板')
        sleep(3)
        flag = not ddos_cluster_page.verify_element_exist('xpath', '//span[text()="暂无数据"]', time_wait=4)
        while flag:
            ddos_cluster_page.click_all()
            ddos_cluster_page.click_delete()
            with allure.step('验证删除成功'):
                msg = ddos_cluster_page.get_success_message('操作成功')
                assert msg, '删除失败'
            flag = not ddos_cluster_page.verify_element_exist('xpath', '//span[text()="暂无数据"]', time_wait=4)


    @allure.story('测试新增集群')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('cluster_name,descp,start',[('绍兴BGP集群','集群描述:新建启用的集群', 1),('测试集群','描述：新建不启用的集群', 0)])
    #@pytest.mark.skip
    def test_new_cluster(self, cluster_name, descp, start, browser):
        ddos_list = browser[1]['ddos任务列表']
        ddos_cluster_page = browser[1]['ddos集群管理']
        ddos_cluster_page.refresh()
        ddos_list.click_menu('集群管理')
        ddos_cluster_page.click_new_cluster()
        ddos_cluster_page.fill_cluster_table(cluster_name, descp, start)
        ddos_cluster_page.click_save()
        result = ddos_cluster_page.verify_element_exist('xpath','//td/div[contains(text(),"%s")]'%(cluster_name))
        assert result,'新增集群失败！'
        if start == 1:
            result_start = ddos_cluster_page.verify_text('xpath', '//td/div[contains(text(),"%s")]/../../td[4]/div/span'%(cluster_name), '启用')
            assert result_start,print('集群状态不是启用')
        else:
            result_end = ddos_cluster_page.verify_text('xpath', '//td/div[contains(text(),"%s")]/../../td[4]/div/span'%(cluster_name), '禁用')
            assert result_end, print('集群状态不是禁用')

    @allure.story('测试新增配置模板')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('model_name, descp, copy_model', [('模板1', '默认模板', ''), ('模板2', '默认模板', '')])
    #@pytest.mark.skip
    def test_new_model(self, model_name, descp, copy_model, browser):
        ddos_list = browser[1]['ddos任务列表']
        ddos_cluster_page = browser[1]['ddos集群管理']
        ddos_model = browser[1]['ddos配置模板']
        ddos_cluster_page.refresh()
        ddos_list.click_menu('配置模板')
        ddos_model.click_new_model()
        ddos_model.fill_model(model_name, descp, copy_model)
        ddos_model.click_save()
        result = ddos_cluster_page.verify_element_exist('xpath', '//td/div[contains(text(),"%s")]' % (model_name))
        assert result, '新增配置模板失败！'

#     # @pytest.mark.test
    @allure.story('验证必填项不填写不能正常新增防御域，IP段不在范围内不能新增成功')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=8)
    #@pytest.mark.skip
    @pytest.mark.parametrize(
        "defence_domain_name, ips, alarm, alarm_type, cluster_name, model_name, contect, description",
        [('', '', '', '', '', '', '', ''), ('测试新增防御域1', '', '', '', '', '', '', '只填写名称'),
         ('测试新增防御域1', '39.98.36.1-11', '999', '1', '', '', '', '只不填写集群'),
         ('测试新增防御域1', '', '999', '1', '绍兴BGP', '', '', '不填写IP'),
         ('测试新增防御域1', '22.22.22.22', '999', '1', '绍兴BGP', '', '', '错误的IP段')])
    def test_new_defence_domain_fail(self,defence_domain_name, ips, alarm, alarm_type, cluster_name, model_name, contect, description, browser):
        driver = browser[0]
        ddos_list = browser[1]['ddos任务列表']
        ddos_list.refresh()
        ddos_list.click_menu('业务列表')
        ddos_list.click_new_domain()
        #'填写防御域信息：防御域名称：{1} ;防御域IP：{2};告警阈值:{3};告警类型:{4};集群:{5};模板:{6};联系人:{7};描述:{8}'
        ddos_list.fill_defence_domain(defence_domain_name, ips, alarm, alarm_type, cluster_name, model_name, contect, description)
        ddos_list.click_save()
        if '错误的IP段' in description:
            result = ddos_list.get_warning_message('IP[22.22.22.22]不在套餐配置的可用IP段内')
            assert result,'未提示IP段错误'
        else:
            result = ddos_list.verify_element_exist('xpath','//div[@class="el-form-item__error"]',time_wait=5)
            assert result,'必填项未填写没有提示'

    @allure.story('验证各种格式的IP都能新增防御域成功')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=9)
    #@pytest.mark.skip
    @pytest.mark.parametrize(
        "defence_domain_name, ips, alarm, alarm_type, cluster_name, model_name, contect, description",
        [('IP段格式的防御域', '39.98.36.0/30', '1', '1', '绍兴BGP集群', '模板1', '赵雅静', ''),
         ('CIDR格式的防御域', '39.98.36.201-224', '1', '1', '绍兴BGP集群', '模板1', '赵雅静', ''),
         ('单IP的防御域', '39.98.36.106', '1', '100', '绍兴BGP集群', '模板1', '赵雅静', ''),
         ('多个单IP的防御域', '39.98.36.100\n'
                       '39.98.36.101\n'
                       '39.98.36.102\n', '1', '100', '绍兴BGP集群', '模板1', '赵雅静', '')])
    def test_new_defence_domain_success(self,defence_domain_name, ips, alarm, alarm_type, cluster_name, model_name, contect, description, browser):
        driver = browser[0]
        ddos_list = browser[1]['ddos任务列表']
        ddos_list.refresh()
        ddos_list.click_menu('业务列表')
        ddos_list.click_new_domain()
        #'填写防御域信息：防御域名称：{1} ;防御域IP：{2};告警阈值:{3};告警类型:{4};集群:{5};模板:{6};联系人:{7};描述:{8}'
        ddos_list.fill_defence_domain(defence_domain_name, ips, alarm, alarm_type, cluster_name, model_name, contect, description)
        ddos_list.click_save()
        result = ddos_list.get_success_message('操作成功')
        assert result,'新增防御域失败'
        with allure.step('验证防御域确实新增成功'):
            result_add = ddos_list.verify_element_exist('xpath',
                                                            '//div[contains(text(),"%s")]' % (defence_domain_name))
            assert result_add, '实际上没有新增成功'


    @allure.story('验证与已有防御域IP重复的不能新增成功')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=10)
    #@pytest.mark.skip
    @pytest.mark.parametrize(
        "defence_domain_name, ips, alarm, alarm_type, cluster_name, model_name, contect, description",
        [('重复-IP段格式的防御域', '39.98.36.1', '1', '1', '绍兴BGP集群', '模板1', '赵雅静', '从IP段格式的IP中取一个'),
         ('重复-CIDR格式的防御域', '39.98.36.224-226', '1', '1', '绍兴BGP集群', '模板1', '赵雅静', '范围有交集'),
         ('重复-单IP的防御域', '39.98.36.106', '1', '100', '绍兴BGP集群', '模板1', '赵雅静', '单个重复'),
         ('重复-多个单IP的防御域', '39.98.36.100\n'
                       '39.98.36.101\n'
                       '39.98.36.103\n', '1', '100', '绍兴BGP集群', '模板1', '赵雅静', '多个中存在一个重复')],
    ids=["重复-IP段格式的防御域:从IP段格式的IP中取一个","重复-CIDR格式的防御域:范围有交集","重复-单IP的防御域","重复-多个单IP的防御域:多个中存在一个重复"])
    def test_new_defence_domain_repeat(self, defence_domain_name, ips, alarm, alarm_type, cluster_name, model_name,
                                        contect, description, browser):
        driver = browser[0]
        ddos_list = browser[1]['ddos任务列表']
        ddos_list.refresh()
        ddos_list.click_menu('业务列表')
        ddos_list.click_new_domain()
        # '填写防御域信息：防御域名称：{1} ;防御域IP：{2};告警阈值:{3};告警类型:{4};集群:{5};模板:{6};联系人:{7};描述:{8}'
        ddos_list.fill_defence_domain(defence_domain_name, ips, alarm, alarm_type, cluster_name, model_name, contect,
                                      description)
        ddos_list.click_save()
        result = ddos_list.get_warning_message('操作失败')
        assert result, '重复的防御域增加成功'
        ddos_list.refresh()
        with allure.step('验证重复的IP不能新增成功'):
            result_add = ddos_list.verify_element_not_exist('xpath','//div[contains(text(),"%s")]'%(defence_domain_name))
            assert result_add,'实际上新增成功'

    @allure.story('测试给启用集群新增设备')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=11)
    @pytest.mark.parametrize('device_ip, start, cpu, mem, network_card , alarm_type, alarm_person, desc',
                             [('45.250.34.134', 1, '60', '60', 1, 1, '赵雅静', '描述'),
                            ('45.250.34.133', 1, '60', '60', 1, 1, '赵雅静', '描述'),
                             ('45.250.34.132', 1, '60', '60', 1, 1, '赵雅静', '描述'),
                             ('45.250.34.131', 1, '60', '60', 1, 1, '赵雅静', '描述')])
    #@pytest.mark.skip
    def test_add_device(self, device_ip, start, cpu, mem, network_card , alarm_type, alarm_person, desc, browser):
        driver = browser[0]
        ddos_list = browser[1]['ddos任务列表']
        ddos_cluster = browser[1]['ddos集群管理']
        ddos_list.refresh()
        ddos_list.click_menu('集群管理')
        ddos_cluster.click_configure_device('绍兴BGP集群')
        ddos_cluster.click_new_device()
        ddos_cluster.fill_device_table(device_ip, start, cpu, mem, network_card , alarm_type, alarm_person, desc)
        ddos_cluster.click_device_save()
        with allure.step('验证设备新增成功'):
            ddos_cluster.verify_element_exist('xpath','//div[text()="%s"]'%(device_ip),time_wait=5)

    @allure.story('测试给禁用集群新增设备')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=12)
    @pytest.mark.parametrize('device_ip, start, cpu, mem, network_card , alarm_type, alarm_person, desc',
                             [('45.250.34.12', 0, '60', '60', 1, 1, '赵雅静', '描述'),
                              ('45.250.34.11', 1, '60', '60', 0, 1, '赵雅静', '描述'),
                              ('45.250.34.10', 1, '99', '99', 1, 2, '赵雅静', '描述'),
                              ('45.250.34.9', 1, '60', '60', 1, 1, '', '告警接收人不能为空'),
                              ('123', 1, '60', '60', 1, 1, '赵雅静', '设备IP格式错误'),
                              ('', 1, '60', '60', 1, 1, '赵雅静', '设备IP不能为空'),
                              ('45.250.34.132', 1, '60', '60', 1, 1, '赵雅静', '设备已存在')])
    #@pytest.mark.skip
    def test_add_device_disabled(self, device_ip, start, cpu, mem, network_card, alarm_type, alarm_person, desc, browser):
        driver = browser[0]
        ddos_list = browser[1]['ddos任务列表']
        ddos_cluster = browser[1]['ddos集群管理']
        ddos_list.refresh()
        ddos_list.click_menu('集群管理')
        ddos_cluster.click_configure_device('测试集群')
        ddos_cluster.click_new_device()
        ddos_cluster.fill_device_table(device_ip, start, cpu, mem, network_card, alarm_type, alarm_person, desc)
        ddos_cluster.click_device_save()
        if desc == '告警接收人不能为空':
            with allure.step('验证告警接收人为空的时候不能新增成功'):
                ddos_cluster.get_warning_message('告警接收人不能为空')
        elif desc == '设备IP不能为空':
            with allure.step('验证设备IP为空的时候不能新增成功'):
                ddos_cluster.get_warning_message('清洗设备IP不能为空')
        elif desc == '设备IP格式错误':
            with allure.step('验证设备IP格式错误的时候不能新增成功'):
                ddos_cluster.get_warning_message('清洗设备IP存在不支持格式')
        elif desc == '设备已存在':
            with allure.step('验证设备已经存在于其他集群  不能新增成功'):
                ddos_cluster.get_warning_message('设备已存在')
        else:
            with allure.step('验证设备新增成功'):
                ddos_cluster.verify_element_exist('xpath','//div[text()="%s"]'%(device_ip),time_wait=5)
    #
    # @allure.story('测试设备失联的情况下能收到告警')
    # #@pytest.mark.skip
    # def test_device_loss(self):
    #     pass
    #
    @allure.story('测试设备的禁用--未使用状态')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=13)
    #@pytest.mark.skip
    def test_disable_device(self, browser):
        driver = browser[0]
        ddos_list = browser[1]['ddos任务列表']
        ddos_cluster = browser[1]['ddos集群管理']
        ddos_list.refresh()
        ddos_list.click_menu('集群管理')
        ddos_cluster.click_configure_device('测试集群')
        sleep(1)
        ddos_cluster.click_all()
        ddos_cluster.click_disabled()
        num = len(ddos_cluster.find_elements('xpath','//tbody//tr'))
        result = True
        sleep(3)
        for i in range(0,num):
            result = result and ddos_cluster.verify_text('xpath', '//tbody//tr[%s]/td[5]//span'%(i+1), '禁用')
        assert result,'全部变成禁用'



    @allure.story('测试设备的启用')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=14)
    #@pytest.mark.skip
    def test_enable_device(self, browser):
        driver = browser[0]
        ddos_list = browser[1]['ddos任务列表']
        ddos_cluster = browser[1]['ddos集群管理']
        ddos_list.refresh()
        ddos_list.click_menu('集群管理')
        ddos_cluster.click_configure_device('测试集群')
        sleep(1)
        ddos_cluster.click_all()
        ddos_cluster.click_start()
        num = len(ddos_cluster.find_elements('xpath', '//tbody//tr'))
        result = True
        sleep(3)
        for i in range(0, num):
            result = result and ddos_cluster.verify_text('xpath', '//tbody//tr[%s]/td[5]//span' % (i + 1), '启用')
        assert result, '全部变成启用'

    @allure.story('测试设备的删除--未使用状态')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=15)
    @pytest.mark.parametrize('device',['45.250.34.12'])
    #@pytest.mark.skip
    def test_delete_device(self, device, browser):
        driver = browser[0]
        ddos_list = browser[1]['ddos任务列表']
        ddos_cluster = browser[1]['ddos集群管理']
        ddos_list.refresh()
        ddos_list.click_menu('集群管理')
        ddos_cluster.click_configure_device('测试集群')
        sleep(1)
        ddos_cluster.click_device_check_box(device)
        ddos_cluster.click_delete()
        sleep(3)
        result = ddos_cluster.verify_element_not_exist('xpath', '//div[contains(text(),"%s")]/ancestor::tr/td[1]//label'%device)
        assert result, '成功删除一个'

    @allure.story('测试防御域引用模板之后会展示在配置模板中')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=16)
    @pytest.mark.parametrize('device', ['45.250.34.12'])
    #@pytest.mark.skip
    def test_domain_model(self, device, browser):
        ddos_list = browser[1]['ddos任务列表']
        ddos_list.refresh()
        ddos_list.click_menu('业务列表')
        model_defence_dict = {}
        row_num = len(ddos_list.find_elements('xpath', '//tbody/tr'))
        for i in range(0,row_num):
            model_name = ddos_list.find_element('xpath', '//tbody/tr[%s]/td[4]/div/span'%(i + 1)).text
            defence_name = ddos_list.find_element('xpath', '//tbody/tr[%s]/td[3]'%(i + 1)).text
            if model_name != '':
                if model_name in model_defence_dict.keys():
                    defence_list = model_defence_dict[model_name]
                    defence_list.append(defence_name)
                    model_defence_dict.update({model_name: deepcopy(defence_list)})
                else:
                    defence_list = []
                    defence_list.append(defence_name)
                    model_defence_dict.update({model_name: deepcopy(defence_list)})
        ddos_list.refresh()
        ddos_list.click_menu('配置模板')
        sleep(2)
        row_num = len(ddos_list.find_elements('xpath', '//tbody/tr'))
        result = True
        for i in range(0,row_num):
            model_name = ddos_list.find_element('xpath', '//tbody/tr[%s]/td[2]/div'%(i + 1), time_wait=5).text
            if model_name in model_defence_dict.keys():
                defence_list = model_defence_dict[model_name]
                for item in defence_list:
                    result = result and ddos_list.verify_element_exist('xpath', '//tbody/tr[%s]/td[4]/div/span/span[contains(text(),"%s")]'%(i + 1, item))
            else:
                result = result and ddos_list.verify_text('xpath', '//tbody/tr[%s]/td[4]/div'%(i + 1), '-')
        assert result,'配置模板中展示的集群不正确'


    @allure.story('测试修改配置模板之后，引用了配置模板的防御域的配置全部修改')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=17)
    @pytest.mark.parametrize('model_name', ['模板1'])
    # #@pytest.mark.skip
    # @pytest.mark.test
    def test_modify_conf(self, model_name, browser):
        ddos_list = browser[1]['ddos任务列表']
        ddos_cluster = browser[1]['ddos集群管理']
        ddos_model = browser[1]['ddos配置模板']
        ddos_conf = browser[1]['ddos策略配置']
        ddos_list.refresh()
        ddos_list.click_menu('配置模板')
        ddos_model.click_modify_conf(model_name)
        sleep(3)
        ddos_conf.click_tcp_bps_limit_switch('ON')#将目的IP TCP限速 改成开启的状态
        ddos_conf.modify_tcp_bps_limit('3000')#将目的IP tcp限速的值 改成3000
        ddos_conf.click_save()
        sleep(3)
        ddos_conf.switch_to_UDP()#切换到UDP
        ddos_conf.modify_udp_bps_threshold('100')#UDP Flood 防御 阈值
        ddos_conf.modify_udp_bps_limit('100')#UDP Flood 防御 限速
        ddos_conf.click_save()
        sleep(4)
        ddos_conf.switch_to_ICMP()
        ddos_conf.modify_icmp_protection_switch('ON')#打开ICMP增强防御
        ddos_conf.modify_src_icmp_stats_time('999')# ICMP Flood 防御	时间
        ddos_conf.modify_src_icmp_pps_min('999')#修改ICMP Flood 防御 阈值
        ddos_conf.click_save()
        sleep(3)
        ddos_conf.switch_to_DNS()
        ddos_conf.click_dns_protection_switch('ON')
        ddos_conf.click_save()
        sleep(3)
        ddos_conf.switch_to_Other()
        ddos_conf.modify_other_bps_threshold('100')
        ddos_conf.modify_other_bps_limit('100')
        ddos_conf.click_save()
        sleep(3)
        ddos_conf.switch_to_black_list()
        ddos_conf.modify_src_trust_timeout('3000')
        ddos_conf.click_save()
        sleep(4)
        ddos_conf.switch_to_threat()
        ddos_conf.click_botip_filter_switch('ON')
        ddos_conf.click_save()
        sleep(4)
        ddos_conf.switch_to_accurate()
        ddos_conf.click_new_rule()
        ddos_conf.fill_accurate('默认规则001', 'TCP', '放行')
        sleep(4)
        #开始验证所有引用了这一模板的防御域全部都修改了
        ddos_conf.refresh()
        sleep(4)
        ddos_list.click_menu('业务列表')
        row_num = len(ddos_list.find_elements('xpath', '//tbody/tr'))
        for i in range(0, row_num-1):
            ddos_conf.refresh()
            ddos_list.click_menu('业务列表')
            sleep(4)
            model_name_cur = ddos_list.find_element('xpath', '//tbody/tr[%s]/td[4]/div/span' % (i + 1)).text
            defence_name = ddos_list.find_element('xpath', '//tbody/tr[%s]/td[3]/div' % (i + 1)).text
            if model_name_cur == model_name:
                ddos_list.click_modify_conf(defence_name)
                sleep(4)
                result = ddos_conf.get_tcp_bps_limit_switch()  # 将目的IP TCP限速 改成开启的状态
                assert result == 'ON'
                result = ddos_conf.get_tcp_bps_limit()  # 将目的IP tcp限速的值 改成3000
                assert result == '3000'
                sleep(1)
                ddos_conf.switch_to_UDP()  # 切换到UDP
                sleep(1)
                result = ddos_conf.get_udp_bps_threshold()  # UDP Flood 防御 阈值
                assert result == '100'
                result = ddos_conf.get_udp_bps_limit()  # UDP Flood 防御 限速
                assert result == '100'
                ddos_conf.switch_to_ICMP()
                sleep(1)
                result = ddos_conf.get_icmp_protection_switch()  # 打开ICMP增强防御
                assert result == 0
                result = ddos_conf.get_src_icmp_stats_time()  # ICMP Flood 防御	时间
                assert result == '60'
                result = ddos_conf.get_src_icmp_pps_min()  # 修改ICMP Flood 防御 阈值
                assert result == '999'
                ddos_conf.switch_to_DNS()
                sleep(1)
                result = ddos_conf.get_dns_protection_switch()
                assert result == 'ON'
                ddos_conf.switch_to_Other()
                sleep(1)
                result = ddos_conf.get_other_bps_threshold()
                assert result == '100'
                result = ddos_conf.get_other_bps_limit()
                assert result == '100'
                ddos_conf.switch_to_black_list()
                result = ddos_conf.get_src_trust_timeout()
                assert result == '3000'
                ddos_conf.switch_to_threat()
                sleep(1)
                result = ddos_conf.get_botip_filter_switch()
                assert result == 'ON'
                ddos_conf.switch_to_accurate()
                sleep(1)
                result = ddos_conf.verify_text('xpath', '//tbody/tr[last()]/td[3]/div', '默认规则001')
                assert result
                i += 1



















