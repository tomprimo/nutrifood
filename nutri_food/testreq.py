import requests

dico = {}
categories = ['breakfast_cereals','drinks','coffee','cheeses','milk']

for category in categories:
    r = requests.get(f'https://world.openfoodfacts.org/category/{category}.json&limit=100')
    dico.update({category : r.json()})
print(dico)
