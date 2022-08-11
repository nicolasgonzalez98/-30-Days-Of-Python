from countries_data import paises as countries

def by_name(e):
    return e['capital'] 

name = sorted(countries, key=by_name, reverse=False)

capital = sorted(countries, key=lambda x:x['capital'])

population = sorted(countries, key=lambda x : x['population'])

