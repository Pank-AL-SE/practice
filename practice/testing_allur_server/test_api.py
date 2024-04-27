"""
first_test_case (valid test)
1) create new project (POST ../projects) check: (GET ../projects)
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




class Test_API:
   
    @pytest.fixture
    def test(self): 
        with allure.step("testing_invalid_coords"):      
            assert 0



    
    