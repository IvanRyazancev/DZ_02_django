from django.core.management.base import BaseCommand
from dz2app.models import Client
class Command(BaseCommand):
    help = "Update user name by id."
    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')
        parser.add_argument('client', type=str, help='User name')
    def handle(self, *args, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('client')
        client = Client.objects.filter(id=id).first()
        client.name = name
        client.save()
        self.stdout.write(f'{client}')