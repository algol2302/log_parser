from django.core.management.base import BaseCommand

from ...utils.crawler import download_mandates


class Command(BaseCommand):
    help = 'Runs scrapping task'

    def handle(self, *args, **options):
        print(download_mandates())
