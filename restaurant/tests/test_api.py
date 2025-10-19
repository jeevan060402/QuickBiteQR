from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from restaurant.models import Restaurant, Table, MenuCategory, MenuItem


class APITests(APITestCase):
    def setUp(self):
        User = get_user_model()
        u = User.objects.create_user('u1')
        r = Restaurant.objects.create(owner=u, name='R', slug='r')
        cat = MenuCategory.objects.create(restaurant=r, name='C')
        self.item = MenuItem.objects.create(category=cat, name='I', price=5.0)
        self.table = Table.objects.create(restaurant=r, table_number=1)

    def test_menu(self):
        url = reverse('menu-list')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_order_table_not_ready(self):
        url = reverse('create-order')
        self.table.status = 'offline'
        self.table.save()
        res = self.client.post(url, {'table_uuid': str(self.table.uuid), 'items': [{'menu_item': self.item.id, 'quantity': 1}]}, format='json')
        self.assertEqual(res.status_code, 400)
