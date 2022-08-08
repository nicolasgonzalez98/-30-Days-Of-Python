from random import randint
from string import ascii_letters, digits
from random import randint
from ex1 import rgb_color_gen as rgb


def list_of_hexa_colors(cant):
    total = []
    str_mother = digits + ascii_letters[0:6]
    hexa = '#'

    while len(total)<cant:
        while(len(hexa) < 7):
            hexa += str_mother[randint(0, len(str_mother)-1)]
        total.append(hexa)
        hexa = '#'
    
    return total

def list_of_rgb_colors(cant):
    total = []
    while len(total)<cant:
        total.append(rgb())
    return total

def generate_colors(type, cant):
    type = type.lower()
    
    if(type == 'hexa' or type == 'rgb'):
        if type == 'hexa':
            return list_of_hexa_colors(cant)
        else:
            return list_of_rgb_colors(cant)
    else:
        return 'Ingresaste un tipo invalido de dato'
    
##print(list_of_hexa_colors(2))
##print(list_of_rgb_colors(2))

##print(generate_colors('hexa',2))



