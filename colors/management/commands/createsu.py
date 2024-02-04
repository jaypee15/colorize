from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

import os
from dotenv import load_dotenv

load_dotenv()
class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username=os.getenv('DJANGO_SUPERUSER_USERNAME')).exists():
            User.objects.create_superuser(
                username=os.getenv('DJANGO_SUPERUSER_USERNAME'),
                password=os.getenv('DJANGO_SUPERUSER_PASSWORD'),
            )
        print('Superuser has been created.')