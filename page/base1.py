import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import time
import random
from time import sleep
class Base:
    def __init__(self,driver):
        self.driver = driver
    #获取界面的截图
    def get_screen_shot(self,name):
        '''

        :param name: 截图放入报告中的名称
        :return:
        '''
        try:
            random_num = int(random.random() * 10)
            img_path = os.path.join('D:\workspace\pytest1\image',str(time.strftime("%Y%m%d%H%M%S",))+str(random_num) + '.png')
            self.driver.get_screenshot_as_file(img_path)
            img = open(img_path,'rb').read()
            allure.attach(img, name, allure.attachment_type.PNG)
        except BaseException as e:
            print('[error]截图失败'+str(e))

        # 获取元素的截图
    def get_element_shot(self, element, name):
        '''

        :param element: 等待截图的元素
        :param name: 截图放入报告中的名称
        :return:
        '''
        try:
            random_num = int(random.random()*100)
            img_path = os.path.join('D:\workspace\pytest1\image', str(time.strftime("%Y%m%d%H%M%S", ))+str(random_num) + '.png')
            element.screenshot(img_path)
            img = open(img_path, 'rb').read()
            allure.attach(img, name, allure.attachment_type.PNG)
        except BaseException as e:
            print('[error]截图失败' + str(e))

    @allure.step('打开页面:{1}')
    #在浏览器中输入网址
    def open(self,url):
        '''

        :param url: 网址
        :return:
        '''
        try:
            self.driver.get(url)
            time.sleep(2)
        except BaseException as e:
            print('[error]打开浏览器失败！'+str(e))
            self.get_screen_shot('打开浏览器失败')

    @allure.step('查找元素:类型-{1}，定位：{2}')
    #定位1个元素
    def find_element(self, type, path, time_wait=2):
        '''

        :param type: 定位元素的方式
        :param path: 元素的定位
        :param time_wait: 等待元素出现的时间 默认2秒
        :return:定位到的元素
        '''
        try:
            if type == 'id':
                locator = (By.ID,path)
                element = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_element_located(locator))
            elif type == 'name':
                locator = (By.NAME, path)
                element = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_element_located(locator))
            elif type == 'css':
                locator = (By.CSS_SELECTOR, path)
                element = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_element_located(locator))
            elif type == 'xpath':
                locator = (By.XPATH, path)
                element = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_element_located(locator))
            elif type == 'link_text':
                locator = (By.LINK_TEXT, path)
                element = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_element_located(locator))
            elif type == 'class_name':
                locator = (By.CLASS_NAME, path)
                element = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_element_located(locator))
            elif type == 'partial_link_text':
                locator = (By.PARTIAL_LINK_TEXT)
                element = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_element_located(locator))
            else:
                element = ''
                print('[error]no such type!')
            return element
        except BaseException as e:
            print('[error]find_element path fail!---'+str(e))
            self.get_screen_shot('获取单个元素失败')

    @allure.step('查找多个元素:类型-{1}，定位：{2}')
    #定位多个元素
    def find_elements(self,type,path,time_wait=2):
        '''

        :param type: 定位元素的方式
        :param path: 元素定位
        :param time_wait: 等待元素出现的超时时间
        :return:查找到的元素列表
        '''
        try:
            if type == 'id':
                locator = (By.ID, path)
                elements = WebDriverWait(self.driver, time_wait, 0.1).until(
                    EC.presence_of_all_elements_located(locator))
            elif type == 'css':
                locator = (By.CSS_SELECTOR, path)
                elements = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_all_elements_located(locator))
            elif type == 'xpath':
                locator = (By.XPATH, path)
                elements = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_all_elements_located(locator))
            elif type == 'name':
                locator = (By.NAME, path)
                elements = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_all_elements_located(locator))
            elif type == 'link':
                locator = (By.CSS_SELECTOR, path)
                elements = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_all_elements_located(locator))
            elif type == 'class_name':
                locator = (By.CLASS_NAME, path)
                elements = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_all_elements_located(locator))
            elif type == 'partial_link_text':
                locator = (By.PARTIAL_LINK_TEXT, path)
                elements = WebDriverWait(self.driver, time_wait, 0.1).until(EC.presence_of_all_elements_located(locator))
            else:
                elements = ''
                print('[error]no such type!')
            return elements
        except BaseException as e:
            print('[error]find_element path fail!---'+str(e))
            self.get_screen_shot('批量获取元素失败')

    @allure.step('校验界面上是否存在某元素:类型-{1}，定位：{2}')
    def verify_element_exist(self,type,path,time_wait=2):
        '''

        :param type: 定位元素的方式
        :param path: 元素定位
        :param time: 超时时间
        :return:
        '''
        try:
            ele = self.find_elements(type,path,time_wait)
            if ele:
                assert len(ele) > 0
                return True
            else:
                return False
        except BaseException as e:
            print("没有找到相应的元素！"+str(e))
            self.get_screen_shot('该存在的元素不存在')
            return False

    @allure.step('校验界面上确定不存在某元素:类型-{1}，定位：{2}')
    def verify_element_not_exist(self, type, path, time_wait=2):
        '''

        :param type: 定位元素的方式
        :param path: 元素定位
        :param time: 超时时间
        :return:
        '''
        try:
            ele = self.find_elements(type, path, time_wait)
            if len(ele) == 0:
                return True
            else:
                self.get_element_shot(ele,"不该存在的元素存在！")
                return False
        except BaseException as e:
            print("不应该找到相应的元素！" + str(e))
            return True

    @allure.step('校验元素内容:类型-{1}，定位：{2}，内容：{3}')
    def verify_text(self, type, path, ele_text, time_wait=2):
        '''

        :param type: 定位元素的方式
        :param path: 元素定位
        :param time: 超时时间
        :return:
        '''
        try:
            ele = self.find_element(type, path, time_wait)
            print(ele.text)
            assert ele.text == ele_text , '预期获得数据'+ele_text+'实际获得数据'+ele.text+'两者不同！'
            return True
        except BaseException as e:
            print("[error]校验界面元素文本失败，文本与预期不同" + str(e))
            self.get_element_shot(ele,"预期文本与实际不同")
            return False

    @allure.step('校验元素内容是否包含指定的内容:类型-{1}，定位：{2}，内容：{3}')
    def verify_contain_text(self, type, path, ele_text, time_wait=2):
        '''

        :param type: 定位元素的方式
        :param path: 元素定位
        :param time: 超时时间
        :return:
        '''
        try:
            ele = self.find_element(type, path, time_wait)
            sleep(0.1)
            cur_text = ele.text
            assert ele_text in cur_text, '预期数据中包含' + ele_text + '实际获得数据' + cur_text + '！'
            return True
        except BaseException as e:
            print("[error]校验界面元素文本失败，文本不包含预期的值" + str(e))
            self.get_element_shot(ele, "预期文本与实际不同")
            return False

    @allure.step('校验元素属性:类型-{1}，定位：{2}，预期内容{3}，属性：{4}')
    def verify_attr(self, type, path, ele_text, attr, time_wait=2):
        '''

        :param type: 定位方式类型
        :param path: 定位
        :param ele_text:预期的元素属性值
        :param attr: 属性
        :param time_wait: 等待时间
        :return: 返回预期值是否包含在属性值之中 boolean
        '''
        try:
            ele = self.find_element(type, path, time_wait)
            sleep(0.1)
            value = self.driver.execute_script('return arguments[0].%s'%attr,ele)
            assert ele_text in value, '预期获得数据' + ele_text + '实际获得数据' + ele.text + '两者不同！'
            return True
        except BaseException as e:
            print("[error]校验界面元素文本失败，文本与预期不同" + str(e))
            self.get_element_shot(ele, "预期文本与实际不同")
            return False

    @allure.step('获取元素指定属性的值:{2}')
    def get_element_attr(self,ele,attr_name):
        return self.driver.execute_script('return arguments[0].%s'%(attr_name),ele)

    @allure.step('等待元素出现')
    def wait_element_appear(self,locator):
        ele = WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(locator))
        return ele

    @allure.step('等待元素显示')
    def wait_element_invisable(self,locator):
        ele = WebDriverWait(self.driver,10,0.1).until(EC.invisibility_of_element_located(locator))
        return ele

    @allure.step('刷新网页')
    def refresh(self):
        self.driver.refresh()
        sleep(2)

    @allure.step('获取提示信息')
    def get_warning_message(self, text):
        return self.verify_contain_text('xpath', '//div[contains(@class,"warning")]//p', text, time_wait=6)

    @allure.step('获取成功提示信息')
    def get_success_message(self,text):
        return self.verify_contain_text('xpath', '//div[contains(@class,"success")]//p', text, time_wait=6)

