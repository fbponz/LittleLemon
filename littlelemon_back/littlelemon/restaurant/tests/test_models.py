from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_add_menu_item(self):
        menu_item = Menu.objects.create(name="Pasta", price=12.99)
        self.assertEqual(str(menu_item), "Pasta - $12.99")