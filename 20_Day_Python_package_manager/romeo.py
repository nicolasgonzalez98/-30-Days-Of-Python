from itertools import count
import requests

def count_words(text, count):
    palabras = {}

    for w in text.split():
        if w in palabras:
            palabras[w]+=1
        else:
            palabras[w] = 1
    
    total = sorted(palabras.items())
    return sorted(total, key = lambda x:x[1], reverse=True)[:count]
    

romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

response = requests.get(romeo_and_juliet)
texto = response.text

print(count_words(texto, 10))