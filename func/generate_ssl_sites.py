import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import redis
import json
import time




#cd C:\Users\yajing.zhao\AppData\Local\Google\Chrome\Application
#chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\selenium\chrome_temp"
def debug_login():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "D:\\software\\chrome_driver\\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    return driver
num = random.random()*10000
print(int(num))
#生成编号是 1000到9999
def generate_sites():
    file = open('site_names.txt',mode='w')
    for item in range(1000,9999):
        temp_str = str(item) + ".lvluoyun.com" + '\n'
        file.write(temp_str)
    print('end')

def delete_sites():
    driver = debug_login()
    while True:
        try:
            elements = driver.find_elements_by_xpath('//span[contains(text(),"未启用")]/preceding::label[1]')
            for item in elements:
                item.click()
            clear = driver.find_element_by_xpath('//span[contains(text(),"删除")]/..')
            clear.click()
            ok = driver.find_element_by_xpath('//span[contains(text(),"确定")]/..')
            ok.click()
            a = WebDriverWait(driver,30,0.1).until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"el-message--success") and contains(@role,"alert")]')))
            if a:
                sleep(10)
                # next_page = driver.find_element_by_xpath('//button[contains(@class,"btn-next")]/i')
                # next_page.click()
                driver.execute_script('location.reload()')
                sleep(10)
        except:
            print('123')

def insert_site():
    driver = debug_login()
    with open(r'1234.txt','r') as file:
        string1 = file.readlines()
        for item in string1:
            try:
                i = item.split(':')[0]
                value = item.split(':')[1]
                driver.find_element_by_xpath('//span[text()="添加记录"]/..').click()
                driver.find_element_by_xpath('(//div[contains(text(),"添加记录")]/following::div[contains(@class,"ant-select-enabled")]/div[@role="combobox"])[1]').click()
                driver.find_element_by_xpath('//ul/li[@title="CNAME"]').click()
                driver.find_element_by_xpath('//div/input[@placeholder="请输入主机记录"]').send_keys(str(i))
                driver.find_element_by_xpath('//div/input[@placeholder="请输入记录值"]').send_keys(value)
                driver.find_element_by_xpath('//span[text()="确 认"]/..').click()
            except:
                pass

def get_cname():
    i = 2
    driver = debug_login()
    while True:
        try:
            ele = driver.find_element_by_xpath('//tr[%s]/td[2]//a'%i)
            ele2 = driver.find_element_by_xpath('//tr[%s]/td[4]//div[@role="radiogroup"]//span/a' % i)
            value = ele.text
            a = value.split('.')
            ele2.click()
            ele3 = driver.find_element_by_xpath('//div[text()="复制CNAME"]/parent::div[not(contains(@style,"none"))]')
            time.sleep(1)
            result = ele3.text
            print(a[0]+":"+result.split('\n')[1])
            i += 1
        except BaseException as e:
            pass

def refresh():
    i = 2
    driver = debug_login()
    while True:
        try:
            driver.find_element_by_xpath('//tr[%s]/td[4]//span[contains(text(),"CNAME")]'%i).click()
            driver.find_element_by_xpath('//div[not(contains(@style,"none")) and @role="tooltip"]//a').click()
            i += 1
            time.sleep(0.5)
        except:
            pass




if __name__ == '__main__':
    get_cname()