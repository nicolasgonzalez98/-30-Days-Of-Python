from ast import Try
import requests

response = requests.get('https://restcountries.com/v3.1/all')
countries = response.json()

def order_countries_by_area(countries):
    return sorted(countries, key=lambda x:x['area'], reverse=True)[:10]

def ten_most_languages(countries):
    languages= {}
    for c in countries:
        try:
            for i in c['languages']:
                if c['languages'][i] in languages:
                    languages[c['languages'][i]] += 1
                else:
                    languages[c['languages'][i]] = 1
        except Exception as e:
            pass
    
    return sorted(languages.items(), key= lambda x : x[1], reverse=True)[:10]

def total_languages(countries):
    languages = []

    for c in countries:
        try:
            for i in c['languages']:
                if c['languages'][i] not in languages:
                    languages.append(c['languages'][i])
                else:
                    pass
        except Exception as e:
            pass
    
    
    return len(languages)
# print(order_countries_by_area(countries))
#print(ten_most_languages(countries))

print(total_languages(countries))
