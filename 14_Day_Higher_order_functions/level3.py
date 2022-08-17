from countries_data import paises as countries

def by_name(e):
    return e['capital'] 

# name = sorted(countries, key=by_name, reverse=False)

# capital = sorted(countries, key=lambda x:x['capital'])

# population = sorted(countries, key=lambda x : x['population'])

##Sort out the ten most spoken languages by location.

languages = {}

for pais in countries:
    for language in pais['languages']:
        if language in languages:
            languages[language]+=1
        else:
            languages[language]=1

total = sorted(languages.items())

total = sorted(total, key= lambda x : x[1], reverse=True)
print(total)

espaniol = list(i['name'] for i in countries if 'Spanish' in i['languages'])




