"""
first_test_case (valid test)
1) search test project (GET ../projects/search
2) export some allure_testing (POST ../send-results and GET ../generate-report) 
    check: (GET ../projects/{id}/reports/{path}) 
3) delete our report (GET ../clean-results) check: (GET ../projects/{id}/reports/{path}) 
4) delete our project (DELETE ../pojects/{id}) check: (GET ../projects/search)

second_test_case (invalid test)
1) search non-existent project (GET ../projects/search)
2) delete non-existent project (DELETE ../pojects/{id})
3) create and delete project twice (POST ../projects and DELETE ../pojects/{id}) 
4) create twice the same named projects (POST ../projects)

third_test_case (simple requests)
1) get virsion
2) get swagger
3) get swagger.json
"""


import pytest
import random
import pytest_check
import allure_pytest
import allure
import os, requests, json, base64
from func import *



@allure.epic("Обратное и прямое тестирование http запросов openstreetmap")
class TestAPI: 
    @allure.story("first_test_case")
    @pytest.mark.parametrize("func,step,res", [(search_response(),'search_project', '<Response [200]>')
                                               ])    
    def test_invalid_coords(self, func,step, res): 
        with allure.step(step):      
            pytest_check.equal(func, res)
        



    
    