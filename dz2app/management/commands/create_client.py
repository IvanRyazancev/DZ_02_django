from datetime import datetime
from django.core.management.base import BaseCommand
from dz2app.models import Client, Product, Order


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *clients, **kwargs):
        client = Client(client='Dan', email='email@email.com', phone='0123456789', address='123 456 789',
                        date_registered=datetime.now())

        client.save()
        self.stdout.write(f'{client}')