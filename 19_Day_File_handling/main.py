import json

def most_spoken_languages(filename, length):
    path = '../data/'+filename
    languagues = {}
    with open(path, encoding="UTF8") as file:
        archivo = json.load(file)
        for pais in archivo:
            for lang in pais['languages']:
                if lang in languagues:
                    languagues[lang]+=1
                else:
                    languagues[lang]=1
    total = sorted(languagues.items())
    return sorted(total, key= lambda x : x[1], reverse=True)[:length]

def most_populated_countries(filename, length):
    path = '../data/'+filename
    
    with open(path, encoding="UTF8") as file:
        archivo = json.load(file)
        archivo = list(map(lambda x:dict(country=x['name'], population=x['population']), archivo))
        archivo = sorted(archivo, key=lambda x:x['population'], reverse=True)
            
    return archivo[:length]

#print(most_spoken_languages(filename='countries_data.json', length=3))
#print(most_populated_countries(filename='countries_data.json', length=10))
