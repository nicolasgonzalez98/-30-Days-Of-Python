import requests
import numpy

api_cats = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(api_cats)
cats = response.json()


def weight(cats):
    medias = []
    for cat in cats:
        medias.append((int(cat['weight']['metric'].split()[0]) + int(cat['weight']['metric'].split()[-1])) / 2)
    print('El minimo es: ', min(medias))
    print('El maximo es: ', max(medias))
    print('La media es de: ',numpy.mean(medias))
    print('La median es de: ', numpy.median(medias))
    print('La STD es de: ', numpy.std(medias))

def lifespan(cats):
    years = []
    for cat in cats:
        years.append((int(cat['life_span'].split()[0]) + int(cat['life_span'].split()[-1])) / 2)
    print('El minimo es: ', min(years))
    print('El maximo es: ', max(years))
    print('La media es de: ',numpy.mean(years))
    print('La median es de: ', numpy.median(years))
    print('La STD es de: ', numpy.std(years))
##weight(cats)
lifespan(cats)