import os, requests, json, base64

name_test_project = 'first-test-case'
allure_results_directory = '/res'
allure_server = 'http://localhost:5050'
current_directory = os.path.dirname(os.path.realpath(__file__))

def restucturize_response(response):
    if str(response) == '<Response [404]>':
        return 404
    elif str(response) == '<Response [400]>':
        return 400
    elif str(response) == '<Response [200]>':
        return 200
    elif str(response) == '<Response [201]>':
        return 201
    else:
        return response

def create_project(name_prj):
    ssl_verification = True
    request_body = {
        "id": name_prj
    }

    headers = {'accept': '*/*', 'Content-type': 'application/json'}
    json_request_body = json.dumps(request_body)
    response = requests.post('http://localhost:5050/allure-docker-service/projects',
                             headers=headers, data=json_request_body)

    return restucturize_response(response)

def search_project(name_prj):
    response = requests.get(allure_server + '/allure-docker-service/projects/search?id='
                             +name_prj)

    return restucturize_response(response)

        
def send_test_allure(name_prj,name_dir):
    allure_results_directory = name_dir
    allure_server = 'http://localhost:5050'
    current_directory = os.path.dirname(os.path.realpath(__file__))
    results_directory = current_directory + allure_results_directory
    files = os.listdir(results_directory)
    project_id = name_test_project
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
    response = requests.post(allure_server +
                            '/allure-docker-service/send-results?project_id=' + name_prj,
                            headers=headers, data=json_request_body, verify=ssl_verification)
    json_response_body = json.loads(response.content)
    json_prettier_response_body = json.dumps(json_response_body, indent=4, sort_keys=True)
    return restucturize_response(response)

def gen_our_res(name_prj):
    execution_name = 'execution from my script'
    execution_from = 'http://google.com'
    execution_type = 'teamcity'
    headers = {'Content-type': 'application/json'}
    ssl_verification = True
    response = requests.get(allure_server + '/allure-docker-service/generate-report?project_id=' + 
                            name_prj + '&execution_name=' +
                            execution_name + '&execution_from=' + execution_from + 
                            '&execution_type=' + execution_type, headers = headers, 
                            verify=ssl_verification)
    
    return restucturize_response(response)
    
        
def clean_history(name_prj):
    response = requests.get('http://localhost:5050/allure-docker-service/clean-history?\
                            project_id='+name_prj)
    return restucturize_response(response)


def delete_test_project(name_prj):
    response = requests.delete('http://localhost:5050/allure-docker-service/projects/' + name_prj)
    return restucturize_response(response)

def get_version():

    response = requests.get('http://localhost:5050/allure-docker-service/version')
    
    return restucturize_response(response)
    
def get_swagger():
    response = requests.get('http://localhost:5050/allure-docker-service/swagger')
    return restucturize_response(response)
    
def get_swagger_json():
    headres = {
        'accept': '*/*'
    }
    response = requests.get('http://localhost:5050/allure-docker-service/swagger.json', headers=headres)
    return restucturize_response(response)







print(create_project("test"))
print(search_project("test"))
print(send_test_allure("test","/test_res"))
print(gen_our_res("test"))
print(delete_test_project("test"))


  

