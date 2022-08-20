#Extract all incoming email addresses as a list from the email_exchange_big.txt file.

import re



with open('../data/email_exchanges_big.txt') as f:
    
    lineas = f.read()
    email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", lineas)
    

def find_most_common_words(path, count):
    palabras = {}
    with open(path) as f:
        texto = f.read()
        
        for w in texto.split():
            if w in palabras:
                palabras[w] += 1
            else:
                palabras[w] = 1
    
    total = sorted(palabras.items())
    total = sorted(total, key= lambda x : x[1], reverse=True)
    return total[:count]

print(find_most_common_words('../data/obama_speech.txt',10))
print(find_most_common_words('../data/michelle_obama_speech.txt',10))
print(find_most_common_words('../data/donald_speech.txt',10))
print(find_most_common_words('../data/melina_trump_speech.txt',10))