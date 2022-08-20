import requests





# resultado = count_words(text=response.json(), count=3)

# print(resultado)

url = 'https://restcountries.com/v3.1/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
# status code, success:200
countries = response.json()



