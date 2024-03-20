from django.core.management.base import BaseCommand
from dz2app.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='Хлеб', description='Белый', price=100, amount=16)
        product.save()
        self.stdout.write(f'{product}')

