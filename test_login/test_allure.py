import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
import allure
import pytest
from src.add import add_method
@allure.feature('测试求和功能')
class TestAllure():
    @allure.story('测试整数的求和功能')
    # @pytest.allure.severity(pytest.allure.severity_level.minor)
    @allure.severity("minor")
    @allure.issue("http://192.168.1.1:8080/mantis")
    @allure.testcase("http://192.168.1.1:8080/testlink")
    def test_int(self):
        """
        测试用例test_int，测试目的：整数求和功能正常
        """
        with allure.step('step one:个位'):
            assert add_method(1, 2) == 3
        with allure.step('step two:十位'):
            assert add_method(10, 20) == 40

    @allure.story('测试小数的求和功能')
    # @pytest.allure.severity(pytest.allure.severity_level.normal)
    @allure.issue("http://192.168.1.1:8080/mantis")
    @allure.testcase("http://192.168.1.1:8080/testlink")
    def test_float(self):
        """
         测试用例test_float，测试目的：小数求和功能正常
         """
        assert add_method(1.2, 3.5) == 4.7
        file = open('./test.jpg', 'rb').read()
        allure.attach(file, 'test_img', allure.attachment_type.PNG)