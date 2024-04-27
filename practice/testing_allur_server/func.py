import os, requests, json, base64
allure_server = 'http://localhost:5050'+'/allure-docker-service'
def test_response():
    
    all_projects = '/projects'
    response = requests.get(allure_server + all_projects)
    return str(response)

def search_response():
    search_projects = '/projects/search?id=1'
    response = requests.get(allure_server + search_projects)
    return str(response)



