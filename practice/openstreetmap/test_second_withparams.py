import pytest
import random
import pytest_check 
from first.testing_api import *
from lib_generators import *

class TestAPI:  
    @pytest.mark.parametrize("lat,lon,res", [(generate_invalid_params(),generate_invalid_params(), 400),#
                                             (generate_invalid_params(),generate_invalid_params(), 400),#                                         
                                             ('asdas','asdasd', 400),#
                                             ('25.08051','--30.30000', 400),
                                             ('55 dot 06924','82.91093', 400),
                                             ('-2525.08051','400.000', 'invalid Key')])    
    def test_invalid_coords(self, lat, lon, res):       
        pytest_check.equal(functions.search_in_lat_lon(lat,lon), res)
        
        

    

    @pytest.mark.parametrize("lat,lon,res",[('55.06924','82.91093','Новосибирская область'),
                                            ('25.08051','30.30000','الوادي الجديد'),                                            ])
    def test_valid_coords(self, lat,lon,res):
        assert functions.search_in_lat_lon(lat,lon) == res
    
    
    @pytest.mark.parametrize("input_addr,input_city,res",[('Крeсный проСпЕкТ 222/1','НоВоСибирск', 'no_info'),
                                                          ('😂😂😂😂😂😂😂😂😂😂','😂😂😂😂😂😂😂😂😂😂','no_info'),
                                                          ('630001','НоВоСибирск',400),
                                                          ('Красный проспект','','no_info'),
                                                          ('','НоВоСибирск','no_info')])
    def test_invalid_addr(self,input_addr,input_city,res):
        pytest_check.equal(functions.find_street(input_addr,input_city), res)



    @pytest.mark.parametrize("input_addr,input_city",[('\u0443\u043b\u0438\u0446\u0430\u0020\u0434\u043e\u0431\u0440\u043e\u043b\u044e\u0431\u043e\u0432\u0430\u0020\u0032\u0430','НоВоСибирск'),
                                                      ('630001','НоВоСибирск'),
                                                      ('','Алтай')])
    def test_valid_addr(self,input_addr,input_city):
        a,b = 55.0025574, 82.9422944
        res = functions.find_street(input_addr,input_city)
        c,d = float(res[0]),float(res[1])
        pytest_check.equal(  abs(a-c) <= 0.01, abs(b-d) <= 0.01)
    
    
    
    
    
