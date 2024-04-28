1. first testcase
    1.1. func.py/create_project()
    1.2. func.py/send_test_allure()
    1.3. func.py/send_test_allure()
    1.4. func.py/send_test_allure()

2. second testcase
    2.1. func.py/create_project()
    2.2. func.py/create_project()
    2.3. func.py/delete_test_project()
    2.4. func.py/delete_test_project()
    2.5. func.py/send_invalid_data()

3. third testcase
    3.1. func.py/get_version()
    3.2. func.py/get_swagger()
    3.3. func.py/get_swagger_json()

func.py:
    search_project()
        do: GET /projects/search
        return: 404 - Not Found
                400 - Bad Request
                200 - OK
    create_project()
        do: search_project() and scripts/create.sh or scripts/delete.sh then scripts/create.sh
        return: search_project() = 200 -> True
                search_project() !=200 -> False
    send_test_allure()
        do: POST /send-results
        return: True - OK
                False - Other
    gen_our_res()
        do: GET /generate-report
        return: 404 - Not Found
                400 - Bad Request
                True - OK 
    clean_history()
        do: GET /clean-history
        return: 404 - Not Found
                400 - Bad Request
                True - OK 
    delete_test_project()
        do: scripts/delete.sh
        return: True - OK
                404 - Other
    get_version()
        do: GET /version
        return: 404 - Not Found
                400 - Bad Request
                200 - OK
    get_swagger()
        do: GET /swagger
        return: 404 - Not Found
                400 - Bad Request
                200 - OK
    get_swagger_json()
        do: GET /swagger.json
        return: 404 - Not Found
                400 - Bad Request
                200 - OK
    send_invalid_data()
        do: POST /send-results
        return: True - OK
                False - Other

To run this code: pytest --alluredir=./res test_api.py 