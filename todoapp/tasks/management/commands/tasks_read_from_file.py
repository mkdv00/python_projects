# coding: utf-8
from django.core.management import BaseCommand
from datetime import datetime, timezone
from tasks.models import TodoItem


class Command(BaseCommand):
    help = u"Read tasks from file (one line = one task) and save them to db"

    def add_arguments(self, parser):
        parser.add_argument('--file', dest='input_file', type=str)


    def handle(self, *args, **options):
        now = datetime.now(timezone.utc)
        lines = list()
        try:
            with open(options['input_file'], encoding='utf-8') as file:
                lines = file.readlines()
        except FileNotFoundError as e:
            print("Файл не найден", e)
        else:
            print("Файл найден, продолжаем")

        for line in lines:
            print(line)
