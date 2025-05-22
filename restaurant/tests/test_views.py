from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse

class TestMenuView(TestCase):
    def setup(self):
        Menu.objects.create(title="Pizza", price=12.99, inventory=5)
        Menu.objects.create(title="Pasta", price=8.50, inventory=3)
    
    def test_getall(self):
        menu_items= Menu.objects.all()
        serialized_data = MenuSerializer(menu_items, many=True).data
        response = self.client.get(reverse('menu-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serialized_data)