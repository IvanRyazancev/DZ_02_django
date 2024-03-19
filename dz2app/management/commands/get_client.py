from django.core.management.base import BaseCommand
from dz2app.models import Client


class Command(BaseCommand):
    help = "Get user by id."
    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        client = Client.objects.get(id=id)
        self.stdout.write(f'{client}')
        return client


