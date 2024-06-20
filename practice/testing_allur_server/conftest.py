import pytest
import os, requests, json, base64
import random


class VALID:
    name_prj = ''
    check_dir = '/test_res'
    create_flag = False
    send_flag = False
    delete_flag = False
    clean_flag = False
    gen_flag = False

class INVALID:
    name_prj = ''
    check_dir = '/invalid_res'
    create_flag = False
    send_flag = False
    delete_flag = False
    clean_flag = False
    gen_flag = False

@pytest.fixture(autouse=True, scope='function')
def init_valid_data():
    symbol = 'zxcvbnmasdfghjklqwertyuiop'
    response = VALID
    response.name_prj = ''
    for i in range(6):
        response.name_prj += random.choice(symbol)
    return response


@pytest.fixture(autouse=True, scope='function')
def init_invalid_data():
    symbol = '/*-+?"}:!@#$%'
    response = INVALID
    response.name_prj = ''
    for i in range(6):
        response.name_prj += random.choice(symbol)
    return response

@pytest.fixture(autouse=True, scope='function')
def init_longlong_data():
    symbol = 'a'
    response = INVALID
    response.name_prj = ''
    for i in range(500):
        response.name_prj += random.choice(symbol)
    return response


