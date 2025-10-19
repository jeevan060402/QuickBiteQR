from django.test import TestCase
from django.contrib.auth import get_user_model
from restaurant.models import Restaurant, Table, MenuCategory, MenuItem


class ModelsTest(TestCase):
    def test_restaurant_and_table(self):
        User = get_user_model()
        u = User.objects.create_user('u1')
        r = Restaurant.objects.create(owner=u, name='R', slug='r')
        t = Table.objects.create(restaurant=r, table_number=1)
        self.assertEqual(str(r), 'R')
        self.assertEqual(str(t), 'R - 1')

