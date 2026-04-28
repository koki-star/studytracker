from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = 'Creates an admin user if one does not exist'

    def handle(self, *args, **options):
        username = os.getenv('ADMIN_USERNAME', 'admin')
        email = os.getenv('ADMIN_EMAIL', 'admin@studytracker.com')
        password = os.getenv('ADMIN_PASSWORD')

        if not password:
            self.stdout.write(
                self.style.WARNING('No ADMIN_PASSWORD environment variable set. Skipping admin creation.')
            )
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.SUCCESS(f'Admin user "{username}" already exists')
            )
        else:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(
                self.style.SUCCESS(f'Admin user "{username}" created successfully')
            )
