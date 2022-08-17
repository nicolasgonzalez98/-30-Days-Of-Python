import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

regex = r'[A-Za-z0-9]+'

matches = re.findall(regex, paragraph)

palabras = {}

for p in matches:
    if p in palabras:
        palabras[p] += 1
    else:
        palabras[p] = 1

resultado = sorted(palabras.items(), key= lambda x : x[1], reverse=True)

print(resultado)