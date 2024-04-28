import pytest
import random
import pytest_check
import allure_pytest
import allure
import os, requests, json, base64
from func import *



@allure.epic("Testing docker_allure")
class TestAPI: 
    @allure.story("first_test_case")
    @pytest.mark.parametrize("func,step,res", [(create_project(),'search_project', True),                                               
                                               (send_test_allure(),'send_test_allure',True),
                                               (clean_history(),'clean_history',True),
                                               (delete_test_project(),'delete_test_project()',True)])    
    def test_first_case(self, func,step, res): 
        with allure.step(step):      
            pytest_check.equal(func, res)
    
    @allure.story("second_test_case")
    @pytest.mark.parametrize("func,step,res", [(create_project(),'first_create_project', True),                                               
                                               (create_project(),'second_create_project',False),
                                               (delete_test_project(),'first_delete_project',True),
                                               (delete_test_project(),'second_delete_project',404),
                                               (send_invalid_data(),'send_invalid_data',True)])    
    def test_second_case(self, func,step, res): 
        with allure.step(step):      
            pytest_check.equal(func, res)

        
    @allure.story("third_test_case")
    @pytest.mark.parametrize("func,step,res", [(get_version(),'get_version', True),
                                               (get_swagger(),'get_swagger', True),
                                               (get_swagger_json(),'get_swagger_json', True),])    
    def test_third_case(self, func,step, res): 
        with allure.step(step):      
            pytest_check.equal(func, res)




    
    