from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(name="Pizza", price=10.99, description="Delicious cheese pizza")
        self.menu2 = Menu.objects.create(name="Burger", price=8.99, description="Juicy beef burger")
        self.menu3 = Menu.objects.create(name="Pasta", price=12.99, description="Creamy Alfredo pasta")

    def test_getall(self):
        response = self.client.get('/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)