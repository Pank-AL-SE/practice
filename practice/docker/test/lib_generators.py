import random

def generate_invalid_params():
    invalid_par = ''
    symb = 'zxcvbnm,./asdfghjkl;qwertyuiop[]1234567890-=_+'       
    for _ in range(9):
        invalid_par += random.choice(symb)
    return invalid_par
    
def generate_non_existant():
    non_existant_par = ['']*15
    state = ['улица ',' проспект',' площадь']
    name = ['Центральная','Молодежная', 'Школьная', 'Советская', 'Садовая',
            'Лесная', 'Новая', 'Ленина', 'Мира', 'Набережная', 'И. В.  Абрамова',
            'Авиаконструкторов', 'Авиастроителей', 'Авиаторов', '1905 года', '1942 года',
            'Абельмановская застава', 'Абхазии', 'Авиаторов']
    for i in range(15):
        non_existant_par[i] += random.choice(state)
        if non_existant_par[i] == 'улица ':
            non_existant_par[i]+=' '+random.choice(name)+' '+random(200)
        else:
            non_existant_par[i]+=' '+ random.choice(name)
    print(non_existant_par)
    return non_existant_par
    
def generate_valid_params():
    valid_par = ['']*15

def print_value(value):
    print(value)

print(generate_invalid_params())