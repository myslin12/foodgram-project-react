import csv

from recipes.models import Ingredient
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Заполнение БД ингредиентами"

    def handle(self, *args, **kwargs):
        with open('/app/data/ingredients.csv', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            for row in csvreader:
                Ingredient.objects.get_or_create(
                    name=row[0],
                    measurement_unit=row[1],
                )
