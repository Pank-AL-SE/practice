import os, requests, json, base64

name_test_project = 'first-test-case'
allure_results_directory = '/res'
allure_server = 'http://localhost:5050'
current_directory = os.path.dirname(os.path.realpath(__file__))

def search_project():
    response = requests.get(allure_server + '/allure-docker-service/projects/search?id='
                             +name_test_project)
    if str(response) == '<Response [404]>':
        return 404
    elif str(response) == '<Response [400]>':
        return 400
    elif str(response) == '<Response [200]>':
        return 200
    else:        
        return response
    
def create_project():
    if search_project() == 404:
        os.system("bash scripts/create.sh")        
    elif search_project() == 200:
        os.system("bash scripts/delete.sh")
        os.system("bash scripts/create.sh")
    
    if search_project() == 200:
        return True
    else:
        return False
        
def send_test_allure():
    if create_project() == True:
        allure_results_directory = '/test_res'
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
                                '/allure-docker-service/send-results?project_id=' + project_id,
                                headers=headers, data=json_request_body, verify=ssl_verification)
        json_response_body = json.loads(response.content)
        json_prettier_response_body = json.dumps(json_response_body, indent=4, sort_keys=True)
        return True
    else:
        return False

def gen_our_res():
    project_id = name_test_project
    execution_name = 'execution from my script'
    execution_from = 'http://google.com'
    execution_type = 'teamcity'
    headers = {'Content-type': 'application/json'}
    ssl_verification = True
    response = requests.get(allure_server + '/allure-docker-service/generate-report?project_id=' + 
                            project_id + '&execution_name=' + 
                            execution_name + '&execution_from=' + execution_from + 
                            '&execution_type=' + execution_type, headers = headers, 
                            verify=ssl_verification)
    
    if str(response) == '<Response [404]>':
        return 404
    elif str(response) == '<Response [400]>':
        return 400
    elif str(response) == '<Response [200]>':
        return True
    else:        
        return response
    
        
def clean_history():
    response = requests.get('http://localhost:5050/allure-docker-service/clean-history?\
                            project_id=first-test-case')
    
    if str(response) == '<Response [404]>':
        return 404
    elif str(response) == '<Response [400]>':
        return 400
    elif str(response) == '<Response [200]>':
        return True
    else:        
        return response


def delete_test_project():
    if search_project() == 200:
        os.system("bash scripts/delete.sh")
        return True
    else:
        return 404






  

