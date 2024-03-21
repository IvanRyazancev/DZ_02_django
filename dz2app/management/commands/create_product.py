from django.core.management.base import BaseCommand, CommandError
from dz2app.models import Product

class Command(BaseCommand):
    help = 'Добавляет новый продукт в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('product', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=float)
        parser.add_argument('quantity', type=int)

    def handle(self, *args, **options):
        try:
            product = Product(
                product=options['product'],
                description=options['description'],
                price=options['price'],
                quantity=options['quantity']
            )
            product.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully added product "{product.product}"'))
        except Exception as e:
            raise CommandError(f'Error adding product: {e}')