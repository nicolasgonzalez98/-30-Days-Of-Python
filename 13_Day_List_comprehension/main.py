## Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
nums = [i for i in numbers if i <= 0]

##print(nums)

##Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

result = [n for row in list_of_lists for n in row]
##print(result)

##Using list comprehension create the following list of tuples:

result = [(i, 1, i**1, i**2, i**3, i**4, i **5) for i in range(11)]

##Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

paises = [[n[0].upper(), n[0][:3].upper(), n[1].upper()] for row in countries for n in row] 

##Change the following list to a list of dictionaries:
paises_dict = [{'country':n[0].upper(), 'city':n[1].upper()} for row in countries for n in row]

##Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

result = [n[0]+' '+n[1] for row in names for n in row]
print(result)