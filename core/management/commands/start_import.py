import pathlib

from django.core.management.base import BaseCommand

from ...utils.download import download
from ...utils.parsing import parsing


class Command(BaseCommand):
    help = 'Runs import task'

    def handle(self, *args, **options):
        try:
            options['link'] or options['l']
        except:
            print('Укажите ссылку. См. описание в --help')
        else:
            # реализуем загрузку в самом простом виде без celery
            # проверки на тип файлов не делаем
            # можно реализовать докачивание файлов при разрывах соединений,
            # перезапусках, расписанию и др. случаях

            # делаем временную папку и качаем туда файл
            pathlib.Path('/tmp/log_parser/').mkdir(parents=True, exist_ok=True)
            # TODO переделать хардкод
            step1 = download(options['link'], '/tmp/log_parser/access.log')
            if step1 == 0:
                #  начинаем парсить файл
                parsing()
            else:
                print('Файл загружен с ошибками! Останавливаем работу...')


    def add_arguments(self, parser):
        parser.add_argument(
            '-l',
            '--link',
            action='store',
            help='Ссылка на указанный файл'
        )
