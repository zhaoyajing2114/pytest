#coding = utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread
webdriver.Chrome()
#浏览器配置信息
browsers = [
    # DesiredCapabilities.INTERNETEXPLORER,
    DesiredCapabilities.CHROME,
    DesiredCapabilities.FIREFOX,
    DesiredCapabilities.CHROME,
    DesiredCapabilities.FIREFOX
]

# 创建webdriver驱动
def createDriver(caps):
    return webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=caps)

def start_test(driver):
    #driver.implicitly_wait(3)
    time.sleep(3)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("python")
    driver.find_element_by_id("su").click()
    #driver.implicitly_wait(3)
    time.sleep(3)
    driver.quit()

#开始分布式测试（多个节点同时运行。）
def test_on_nodes():
    threads = []

    for bw in browsers:
        driver = createDriver(bw)
        t = Thread(target=start_test, args=(driver,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("测试运行完成")

if __name__ == '__main__':
    #print(DesiredCapabilities.INTERNETEXPLORER)
    test_on_nodes()