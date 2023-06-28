from django.core.management.base import BaseCommand, CommandError
# from search.models import Question as Poll
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
        
        # for category in categories:
        if len(options['list'])<=5:
            for category in options['list']:
                r = requests.get(f'https://world.openfoodfacts.org/category/{category}.json&limit=100')
                dico.update({category : r.json()})
                self.stdout.write(self.style.SUCCESS('Successfully requested "%s" from api' % category))
        else:
            print('too many categories')
        
        return(str(dico))
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
