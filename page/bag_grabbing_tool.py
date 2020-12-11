#ddos原生清洗 抓包工具
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from func.base import Base
import allure


class Ddos_bag_grabbing_tool(Base):
    @allure.MASTER_HELPER.step('点击新建集群')
    def click_new_cluster(self):
        #点击新增集群
        self.find_element('xpath','//span[text()="新增集群"]/..').click()