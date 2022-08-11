from functools import reduce
from paises import countries


##countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

##Use map to create a new list by changing each country to uppercase in the countries list
countries_upper = list(map(lambda c : c.upper(), countries))

##Use map to create a new list by changing each number to its square in the numbers list
square = list(map(lambda n:n**2, numbers))

##Use map to change each name to uppercase in the names list
names_uppercase = list(map(lambda n:n.upper(), names))

##Use filter to filter out countries containing 'land'.
land_countries = list(filter(lambda c : c.endswith('land'), countries))

##Use filter to filter out countries containing six letters and more in the country list.
six_or_more = list(filter(lambda c : len(c) < 6, countries))

##Use reduce to sum all the numbers in the numbers list.
total = reduce(lambda x,y: x+y, numbers)

##Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

def makesentence(c):
    return ', '.join(c[:-1]) + ' and ' + c[-1] + ' are north European countries'


##Declare a function called categorize_countries that returns a list of countries with some common pattern 
##(you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

def categorize_countries(country, string = 'pt'):
    return country.endswith(string)

total = list(filter(categorize_countries, countries))





