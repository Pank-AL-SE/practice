import random


class VALID:
    name_prj = ''
    check_dir = '../testing_allur_server/test_data/test_res/'
    create_flag = False
    send_flag = False
    delete_flag = False
    clean_flag = False
    gen_flag = False


class INVALID:
    name_prj = ''
    check_dir = '../testing_allur_server/test_data/invalid_res/'
    create_flag = False
    send_flag = False
    delete_flag = False
    clean_flag = False
    gen_flag = False


def gen_valid_data():
    symbol = 'zxcvbnmasdfghjklqwertyuiop'
    response = VALID
    response.name_prj = ''
    for i in range(6):
        response.name_prj += random.choice(symbol)
    return response


def gen_invalid_data():
    symbol = '/%^[]_+'
    response = INVALID
    response.name_prj = ''
    for i in range(6):
        response.name_prj += random.choice(symbol)
    return response


def gen_longlong_data():
    symbol = 'aaaaaaaaaaaa'
    response = VALID
    response.name_prj = ''
    for i in range(6):
        response.name_prj += random.choice(symbol)
    return response