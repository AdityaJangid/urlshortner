from django.core.management.base import BaseCommand, CommandError
from shortener.models import BigUrl

class Command(BaseCommand):
    help = "Refreshes all the BigUrl shortcodes"

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self,*args,**options):
        #  print(options)
        return BigUrl.objects.refresh_shortcodes(items = options['items'])




