import pytest
from selenium import webdriver
import configparser
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def get_driver():
    env = {}
    conf = configparser.ConfigParser()
    conf.read(r'D:\workspace\pytest1\conf\conf.ini',encoding='utf-8')
    print(conf.sections())
    if conf.has_section('adminv6'):
        v6_username = conf.get('adminv6','username')
        env.update({'v6_username': v6_username})
        v6_password = conf.get('adminv6','password')
        env.update({'v6_password': v6_password})
        v6_url = conf.get('adminv6','url')
        env.update({'v6_url': v6_url})
    else:
        print('没有找到adminv6的配置！')

    if conf.has_section('api_environment'):
        url = conf.get('api_environment','url')
        env.update({'url':url})
        username = conf.get('api_environment','username')
        env.update({'username': username})
        password = conf.get('api_environment','password')
        env.update({'password': password})
        success_sign = conf.get('api_environment','login_success_sign')
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        login_success = False
        try_time = 3
        while not login_success and try_time>0:
            try:
                driver.get(url+'/login')
                driver.find_element_by_id('username').send_keys(username)
                driver.find_element_by_id('password').send_keys(password)
                driver.find_element_by_xpath('//button[@type="submit"]').click()
                sleep(2)
                WebDriverWait(driver,5,0.1).until(EC.presence_of_element_located((By.CLASS_NAME,success_sign)))
                login_success = True
            except:
                login_success = False
                try_time = try_time - 1
        if login_success == True:
            return driver,env
        else:
            print('登陆失败！')

    else:
        print('没有找到配置项！')
