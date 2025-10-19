from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from restaurant.models import Restaurant, Table, MenuCategory, MenuItem


class Command(BaseCommand):
    help = 'Seed demo data: demo_owner user, restaurant, categories, menu items, tables'

    def handle(self, *args, **options):
        User = get_user_model()
        user, created = User.objects.get_or_create(username='demo_owner', defaults={'is_staff': True, 'is_superuser': True})
        if created:
            user.set_password('demopass')
            user.save()
        rest, _ = Restaurant.objects.get_or_create(owner=user, defaults={'name': 'Demo Restaurant', 'slug': 'demo-restaurant'})
        cat, _ = MenuCategory.objects.get_or_create(restaurant=rest, name='Mains')
        for i in range(1, 6):
            MenuItem.objects.get_or_create(category=cat, name=f'Demo Item {i}', defaults={'price': 9.99 + i})
        # create tables
        for n in range(1, 6):
            Table.objects.get_or_create(restaurant=rest, table_number=n)
        self.stdout.write(self.style.SUCCESS('Seeded demo data (demo_owner/demopass)'))
