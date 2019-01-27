from django.core.management.base import BaseCommand

from ...utils.import_mandates import import_mandates


class Command(BaseCommand):
    help = 'Runs import task'

    def handle(self, *args, **options):
        print(import_mandates())
