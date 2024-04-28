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
    def test_invalid_coords(self, func,step, res): 
        with allure.step(step):      
            pytest_check.equal(func, res)
        



    
    