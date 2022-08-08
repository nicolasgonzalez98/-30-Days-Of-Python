from random import random, randint
from string import ascii_letters, digits


##Level 1
def random_user_id():
    result = ''
    str_mother = ascii_letters+digits

    while len(result) < 5:
        result += str_mother[randint(0, len(str_mother) - 1)]
    
    return result

def user_id_gen_by_user(count_code = 5, len_code = 16):
    ids = []
    result = ''
    str_mother = ascii_letters+digits
    if(count_code < 1):print('No ingresaste suficientes codigos')

    while(len(ids) < count_code):
        while(len(result) < len_code):
            result += str_mother[randint(0, len(str_mother) - 1)]
        ids.append(result)
        result = ''

    return ids

def rgb_color_gen():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    return f'rgb({r},{g},{b})'
##print(random_user_id())
##print(user_id_gen_by_user())
##print(rgb_color_gen())

