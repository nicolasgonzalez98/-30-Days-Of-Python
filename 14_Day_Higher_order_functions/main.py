countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

##Use map to create a new list by changing each country to uppercase in the countries list
countries_upper = list(map(lambda c : c.upper(), countries))

##Use map to create a new list by changing each number to its square in the numbers list
square = list(map(lambda n:n**2, numbers))

##Use map to change each name to uppercase in the names list
names_uppercase = list(map(lambda n:n.upper(), names))



