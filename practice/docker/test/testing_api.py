import requests
import locale
import json
class functions():

    def find_street(address,city):
        url = 'https://nominatim.openstreetmap.org/search.php?street='+address+'&city='+city+'&format=jsonv2'
        response = requests.get(f"{url}")
        if response.status_code != 200:
            return(response.status_code)
        else:
            res = json.loads(response.content.decode('utf-8'))
            if len(res) == 0:
                return 'no_info'
            else:
                res = [res[0]['boundingbox'][0],res[0]['boundingbox'][3]]
                return res


    def search_in_lat_lon(lat,lon):
        url = 'https://nominatim.openstreetmap.org/reverse?lat='+lat+'&lon='+lon+'&format=jsonv2'
        response = requests.get(f"{url}")
        if response.status_code != 200:
            return response.status_code
        else:
            res = json.loads(response.content.decode('utf-8'))
            if len(res) == 0:
                return 'no_info'
            else:
                if 'error' in res:
                    return 'invalid Key'
                else:
                    return res['address']['state']
        
    

    
        


if __name__ == '__main__':
    print(functions.find_street(address='улица дуси ковальчук 258 красный',city='новосибирскк'))
    print(functions.search_in_lat_len(lat='25000.08051',lon='30.30000'))
    
    