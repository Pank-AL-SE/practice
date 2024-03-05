import pytest
import random
from testing_api import *
from lib_generators import *

class TestAPI:  
    @pytest.mark.parametrize("lat,lon,res", [(generate_invalid_params(),generate_invalid_params(), 400),
                                             (generate_invalid_params(),generate_invalid_params(), 400),
                                             (generate_invalid_params(),generate_invalid_params(), 400),
                                             (generate_invalid_params(),generate_invalid_params(), 400),
                                             (generate_invalid_params(),generate_invalid_params(), 400),
                                             (generate_invalid_params(),generate_invalid_params(), 400),])    
    def test_invalid_coords(self, lat, lon, res):
        assert functions.search_in_lat_lon(lat,lon) == res

    

    @pytest.mark.parametrize("lat,lon,res",[('1','2',3)])
    def test_equal_coords(self, lat,lon,res):
        assert functions.search_in_lat_lon(lat,lon) == res

    

    
    
    
    
    #add analizator
    #keys alur 
