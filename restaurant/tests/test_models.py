from django.test import TestCase
from restaurant.models import Menu, Booking

class TestMenu(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        expected_str = "IceCream costs 80.00 and there are 100 in stock"
        self.assertEqual(str(item), expected_str)

