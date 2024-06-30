from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin_admin@sky.pro',
            first_name='Admin',
            last_name='TB2',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('vfif')
        user.save()
