import pytest
import os, requests, json, base64


@pytest.fixture(autouse=True,scope='class')
def test_up(request):  
    os.system("bash scripts/create_main.sh")  
    allure_results_directory = '/res'
    allure_server = 'http://localhost:5050'
    current_directory = os.path.dirname(os.path.realpath(__file__))
    results_directory = current_directory + allure_results_directory
    files = os.listdir(results_directory)
    project_id = 'testing-allur-server'
    results = []
    for file in files:
        result = {}

        file_path = results_directory + "/" + file

        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as f:
                    content = f.read()
                    if content.strip():
                        b64_content = base64.b64encode(content)
                        result['file_name'] = file
                        result['content_base64'] = b64_content.decode('UTF-8')
                        results.append(result)
            finally :
                f.close()

    headers = {'Content-type': 'application/json'}
    request_body = {
        "results": results
    }
    json_request_body = json.dumps(request_body)
    ssl_verification = True
    response = requests.post(allure_server + '/allure-docker-service/send-results?project_id=' + project_id, headers=headers, data=json_request_body, verify=ssl_verification)
    print("STATUS CODE:")
    print(response.status_code)
    json_response_body = json.loads(response.content)
    json_prettier_response_body = json.dumps(json_response_body, indent=4, sort_keys=True)
    
    yield
    execution_name = 'execution from my script'
    execution_from = 'http://google.com'
    execution_type = 'teamcity'
    response = requests.get(allure_server + '/allure-docker-service/generate-report?project_id=' + project_id + '&execution_name=' + execution_name + '&execution_from=' + execution_from + '&execution_type=' + execution_type, headers=headers, verify=ssl_verification)
    