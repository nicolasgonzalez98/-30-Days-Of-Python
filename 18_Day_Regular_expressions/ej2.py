from ast import Try
import re

def is_valid_variable(variable):
    regExp = r'[^0-9\W][^\W]+'
    
    try:
        
        i, f = re.match(regExp, variable, re.I).span()
        if f == len(variable):
            return True
        else:
            return False
    except Exception:
        return False
    pass


print(is_valid_variable('!firstname'))
print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname'))

