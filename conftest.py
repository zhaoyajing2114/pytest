import pytest
from selenium import webdriver
import configparser
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())
print(sys.path)
from time import sleep
from page.web_security_list import SiteList
from page.login_page import Login_page
from page.adminv6 import Adminv6
from page.ddos_list import Ddos_list
from page.ddos_conf import Ddos_conf
from page.ddos_cluster import Ddos_cluster
from page.ddos_model import Ddos_model
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import allure
import random
import time

_driver = None

@pytest.fixture(scope='session')
def get_cookie():
    conf = configparser.ConfigParser()
    conf.read('./conf/test_conf.ini',encoding='utf-8')
    if conf.has_section('api_environment'):
        url = conf.get('api_environment','url')
        username = conf.get('api_environment','username')
        password = conf.get('api_environment','password')
        success_sign = conf.get('api_environment','login_success_sign')
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        login_success = False
        try_time = 3
        while not login_success and try_time>0:
            try:
                driver.get(url)
                driver.find_element_by_id('username').send_keys(username)
                driver.find_element_by_id('password').send_keys(password)
                driver.find_element_by_xpath('//button[@type="submit"]').click()
                WebDriverWait(driver,5,0.1).until(EC.presence_of_element_located((By.CLASS_NAME,success_sign)))
                login_success = True
            except:
                login_success = False
                try_time = try_time - 1
        if login_success == True:
            cookie = driver.get_cookie()
            return cookie
        else:
            print('登陆失败！')
    else:
        print('没有找到配置项！')

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                random_num = int(random.random() * 10)
                img_path = os.path.join('D:\workspace\pytest1\image',
                                        str(time.strftime("%Y%m%d%H%M%S", )) + str(random_num)+'.png')
                _driver.get_screenshot_as_file(img_path)
                img = open(img_path, 'rb').read()
                allure.attach(img,"失败截图", allure.attachment_type.PNG)
                print('123')

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

@pytest.fixture(scope='session')#,autouse=True
def browser():
    global _driver
    env = {}
    if _driver is None:
        _driver = webdriver.Chrome()
        _driver.implicitly_wait(5)
        _driver.maximize_window()
    #开始初始化页面
    page_dict = {}
    page = Login_page(_driver)
    page_dict.update({"登录页面":page})
    v6page = Adminv6(_driver)
    page_dict.update({"订单管理系统": v6page})
    site_list_page = SiteList(_driver)
    page_dict.update({"web安全加速": site_list_page})
    ddos_list = Ddos_list(_driver)
    page_dict.update({"ddos任务列表": ddos_list})
    ddos_cluster = Ddos_cluster(_driver)
    page_dict.update({"ddos集群管理": ddos_cluster})
    ddos_conf = Ddos_conf(_driver)
    page_dict.update({"ddos策略配置": ddos_conf})
    ddos_model = Ddos_model(_driver)
    page_dict.update({"ddos配置模板":ddos_model})
    #开始获取配置文件中的内容
    conf = configparser.ConfigParser()
    conf.read(r'D:\workspace\pytest1\conf\test_conf.ini', encoding='utf-8')
    print(conf.sections())
    if conf.has_section('adminv6'):
        v6_username = conf.get('adminv6', 'username')
        env.update({'v6_username': v6_username})
        v6_password = conf.get('adminv6', 'password')
        env.update({'v6_password': v6_password})
        v6_url = conf.get('adminv6', 'url')
        env.update({'v6_url': v6_url})
    else:
        print('没有找到adminv6的配置！')
    if conf.has_section('api_environment'):
        url = conf.get('api_environment', 'url')
        env.update({'url': url})
        username = conf.get('api_environment', 'username')
        env.update({'username': username})
        password = conf.get('api_environment', 'password')
        env.update({'password': password})
        success_sign = conf.get('api_environment', 'login_success_sign')
        env.update({'success_sign': success_sign})
    else:
        print('没有找到api_environment的配置！')
    if conf.has_section('test_params'):
        site_names = []
        site_names_str = conf.get('test_params','site_names')
        for item in site_names_str.split('|'):
            site_names.append(item)
        env.update({'site_names': site_names})
    else:
        print('没有找到test_params模块')
    yield (_driver,page_dict,env)
    print("1111111111")
    # _driver.quit()
    #暂时不关闭 方便查看错误在哪里



