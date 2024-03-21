from django.core.management.base import BaseCommand
from dz2app.models import Order, Client, Product
from random import randint, choice


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser, product_keys=None):
        parser.add_argument('user_key', type=int, help='UserID')
        parser.add_argument('product_keys', nargs='+', type=int, help='ProductIDs')

    def handle(self, *args, **kwargs):
        user = Client.objects.get(id=kwargs.get('user_key'))
        product_keys = kwargs.get('product_keys')
        total_price = 0
        for product_key in product_keys:
            product = Product.objects.get(id=product_key)
            total_price += product.price * randint(1, 5)
        order = Order.objects.create(customer=user, total_price=total_price)
        for product_key in product_keys:
            product = Product.objects.get(id=product_key)
            order.products.add(product)
        self.stdout.write(f'Order created: {order}')