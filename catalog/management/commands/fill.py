from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()

        category_list = [
            {'name': 'Куртки', 'description': 'Спортивные куртки'},
            {'name': 'Костюмы', 'description': 'Теплые костюмы'},
            {'name': 'Обувь', 'description': 'Беговые кросовки'},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)
