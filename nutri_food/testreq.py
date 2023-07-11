import requests
from search.models import Product

dico = {}

categories = ['breakfast_cereals','drinks','coffee','cheeses','milk']

for category in categories:

    r = requests.get(f'https://world.openfoodfacts.org/category/{category}.json&limit=100')
    dico.update({category : r.json()})
    # self.stdout.write(self.style.SUCCESS('Successfully requested "%s" from api' % category))

features = {'product_name': None,'ingredients_text':None,'brands':None,'categories':None,'nutriscore_score':None}
l=[]
for key,cat in dico.items():
    # print(cat)
    for p in cat['products']:
        f_temp = features.copy()
        for k, value in f_temp.items():
            try:
                f_temp[k] = p[k]
            except:
                f_temp[k] = None
        product = Product(ingredients = f_temp['ingredients_text'], nutriscore= f_temp['nutriscore_score'],name=f_temp['product_name'],category=f_temp['categories'],brand = f_temp['brand'])
        product.save()
print(l)
    #    for k,v in p.items():
    #        print(k)