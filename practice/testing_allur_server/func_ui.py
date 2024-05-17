import pytest
import random
import pytest_check
import allure_pytest
import allure
import os, requests, json, base64
import selenium 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
def init_max_window():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("http://localhost:5252/allure-docker-service-ui/")
        return driver
    except:
        return(404)
    
def init_project():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("http://localhost:5252/allure-docker-service-ui/projects/2")
        return driver
    except:
        return(404)
    
def init_half_window():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("http://localhost:5252/allure-docker-service-ui/")
        return driver
    except:
        return(404)

def check_title():
    driver = init_max_window()
    if 'Allure Docker Service UI' in driver.title:
        return True
    elif driver == 404:
        return False
    else: 
        return "Unknown Error"

def check_slide_panel():
    driver = init_max_window()
    if driver == 404:
        return "Not Found"
    slide_pannel = driver.find_elements(By.XPATH, '//div/div/div')
    if 'style="visibility: hidden; transform: translateX(-240px);"' not in slide_pannel[6].get_attribute('outerHTML'):
        return "Not found slide_pannel"
        
    btns = driver.find_elements(By.XPATH, '//div//div//header//div/button')
    time.sleep(5)
    btns[0].click()
    time.sleep(5)
    print(slide_pannel[0].get_attribute('outerHTML'))
    if 'style="visibility: hidden; transform: translateX(-240px);"' not in slide_pannel[0].get_attribute('outerHTML'):
        return True
    else:
        return "Slide pannel don't work"

def check_theme():
    driver = init_max_window()
    if driver == 404:
        return "Not Found"
    header = driver.find_elements(By.XPATH, '//div/div/div')
    style1 = str(header[0].get_attribute('outerHTML'))[:19]
    switcher = driver.find_elements(By.XPATH, '//button')
    time.sleep(5)
    switcher[6].click()
    time.sleep(5)
    style2 = str(header[0].get_attribute('outerHTML'))[:19]
    if style1 < style2:
        return True
    elif style1 == style2:
        return "BTN didn't click"
    else:
        return "Unknown Error"
    
def check_language():
    driver = init_max_window()
    if driver == 404:
        return "Not Found"
    switcher = driver.find_elements(By.XPATH, '//button')
    switcher[7].click()    
    time.sleep(5)
    actions = ActionChains(driver)
    actions.move_by_offset(0, 0).perform()
    time.sleep(4)
    actions.click().perform()
    time.sleep(3)
    
def check_window():
    driver = init_half_window()
    if driver == 404:
        return "Not Found"
    header1 = driver.find_elements(By.XPATH, '//button')
    driver = init_max_window()
    if driver == 404:
        return "Not Found"
    header2 = driver.find_elements(By.XPATH, '//button')
    try:
        header1[6].click()
    except:
        res = True
    try:
        header2[6].click()
    except:
        return 'Unknown Button'
    return res


def check_create_project():
    driver = init_max_window()
    if driver == 404:
        return "Not Found"
    
    header = driver.find_elements(By.XPATH, '//button')
    time.sleep(5)
    header[4].click()
    time.sleep(5)
    header1 = driver.find_elements(By.XPATH, '//input')
    header1[3].send_keys("2")
    time.sleep(5)
    header = driver.find_elements(By.XPATH, '//button')
    cnt = 0
    # for i in range(len(header)):
    #     print(str(header[i].get_attribute('outerHTML')))
    #     if '<span class="MuiButton-label">Create</span><span class="MuiTouchRipple-root"></span>' in header[i].get_attribute('outerHTML'):
    #         cnt+=1
    # print(cnt)
    header[16].click()
    time.sleep(5)

def check_send_file():
    driver = init_project()
    if driver == 404:
        return "Not Found"
    header = driver.find_elements(By.XPATH, '//button')
    # cnt = 0
    # for i in range(len(header)):
    #     print(str(header[i].get_attribute('outerHTML')))
    #     if 'Send Results' in header[i].get_attribute('outerHTML'):
    #         print(i)
    # print(cnt)
    header[16].click()
    time.sleep(5)
    header = driver.find_elements(By.XPATH, '//label')
    # cnt = 0
    # for i in range(len(header)):
    #     print(str(header[i].get_attribute('outerHTML')))
    #     if 'Upload Files' in header[i].get_attribute('outerHTML'):
    #         print(i)
    # print(cnt)
    header[0].click()
    time.sleep(5)
    header[0].send_keys("invalid_res/test.txt")
    time.sleep(5)



print(check_send_file())