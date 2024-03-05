import pytest
from testing_api import *

import pytest
@pytest.fixture()
def test_address(request):
    print("Finding in address")
    def test_address_down():
        print("ending_address")
    request.addfinalizer(test_address_down)
    
def test_addr(test_address):
    """mistake in literals"""
    print('test_addr')
    a,b = 55.06924, 82.91093
    res = functions.find_street(address = '      Красный проСпЕкТ 222/1', city = 'НоВоСибирск')
    c,d = float(res[0]),float(res[1])
    assert  abs(a-c) <= 0.01 and abs(b-d) <= 0.01    

def test_lat_len2(test_address):
    """correct"""
    print('test_coords')
    assert functions.search_in_lat_lon(lat='25.08051',lon='30.30000') == 'الوادي الجديد'

def test_lat_len3(test_address):
    """double minusies"""
    print('test_coords')
    assert functions.search_in_lat_lon(lat='25.08051',lon='--30.30000') == 400

def test_addr4(test_address):
    """mistake крЕсный"""
    print('test_addr')
    res = functions.find_street(address = 'Крeсный проСпЕкТ 222/1', city = 'НоВоСибирск')    
    assert  res == 'no_info'

def test_lat_len5(test_address):
    """correct coords"""
    print('test_coords')
    assert functions.search_in_lat_lon(lat='55.06924',lon='82.91093') == 'Новосибирская область'

def test_lat_len6(test_address):
    """with mistake changed . and dot"""

    print('test_coords')
    assert functions.search_in_lat_lon(lat='55 dot 06924',lon='82.91093') == 400

def test_addr7(test_address):
    """whith stickers"""
    print('test_addr')
    a,b = 55.06924, 82.91093
    res = functions.find_street(address = '😂😂😂😂😂😂😂😂😂😂', city = '😂😂😂😂😂😂😂😂😂😂')
    assert  res == 'no_info'

def test_addr8(test_address):
    """postcode changed with  """

    print('test_addr')
    a,b = 55.06924, 82.91093
    res = functions.find_street(address = '630001', city = 'НоВоСибирск')
    assert  res == 400

def test_addr9(test_address):
    """with utf-8 codding"""
    print('test_addr')
    a,b = 55.0025574, 82.9422944
    res = functions.find_street(address = '\u0443\u043b\u0438\u0446\u0430\u0020\u0434\u043e\u0431\u0440\u043e\u043b\u044e\u0431\u043e\u0432\u0430\u0020\u0032\u0430', city = 'НоВоСибирск')
    c,d = float(res[0]),float(res[1])
    assert  abs(a-c) <= 0.01 and abs(b-d) <= 0.01 



def test_addr10(test_address):
    """without input city"""
    print('test_addr')
    a,b = 55.06924, 82.91093
    res = functions.find_street(address = 'Красный проспект', city = '')
    assert  res == 400

def test_addr11(test_address):
    """without input address"""
    print('test_addr')
    a,b = 55.06924, 82.91093
    res = functions.find_street(address = '', city = 'Алтай')
    assert  res == 400

def test_lat_len12(test_address):
    """invalid Key"""
    print('test_coords')
    assert functions.search_in_lat_lon(lat='-2525.08051',lon='400.000') == 'invalid Key'