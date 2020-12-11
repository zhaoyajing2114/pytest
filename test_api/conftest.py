import pytest
from selenium import webdriver
import configparser
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())
print(sys.path)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import allure
import random
import time
import json
@pytest.fixture(scope='session')
def get_conf():
    conf_dict = {}
    conf = configparser.ConfigParser()
    conf.read(r'D:\workspace\pytest1\conf\test_api_conf.ini',encoding='utf-8')
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
            cookie = driver.get_cookies()
            conf_dict.update({'cookie': str(cookie)})
            driver.quit()
        else:
            print('登陆失败！')
    else:
        print('没有找到配置项！')
    if conf.has_section('case'):
        case_path = conf.get('case','file_path')
        conf_dict.update({'case_path':case_path})
    else:
        print('没有找到配置项！')
    yield conf_dict
    print('测试完成')
