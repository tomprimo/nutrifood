from django.core.management.base import BaseCommand, CommandError
# from search.models import Question as Poll
from search.models import Product
import requests

class Command(BaseCommand):
    help = 'gets 100 product for 5 categories'

    def add_arguments(self, parser):
        parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
        # Use like:
    # python arg.py -l 1234 2345 3456 4567

    def handle(self, *args, **options):
        dico = {}
        print(options)
        # categories = ['breakfast_cereals','drinks','coffee','cheeses','milk']
        features = {'product_name': None,'ingredients_text':None,'brands':None,'categories':None,'nutriscore_score':None}
        l=[]
        # for category in categories:
        if len(options['list'])<=5:
            for category in options['list']:
                r = requests.get(f'https://world.openfoodfacts.org/category/{category}.json&limit=100')
                dico.update({category : r.json()})
                
        else:
            print('too many categories')
        
        for key,cat in dico.items():
            print(cat['products'])
            for p in cat['products']:
                f_temp = features.copy()
                print('tftft')
                for k, value in f_temp.items():
                    try:
                        f_temp[k] = p[k]
                        print('oui')
                    except:
                        f_temp[k] = None
                product = Product(ingredients = f_temp['ingredients_text'], nutri_score= f_temp['nutriscore_score'],name=f_temp['product_name'],category=f_temp['categories'],brand = f_temp['brands'])
                product.save()
                l.append(product)
        self.stdout.write(self.style.SUCCESS('Successfully requested "%s" from api' % category))
        return(str(l))
        
        
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
