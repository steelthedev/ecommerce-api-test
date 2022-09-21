
from django.test import TestCase
from .models import Order, OrderItem
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from accounts.models import Profile
from products.models import Product



class TestOrderModel(TestCase):

    def setUp(self) -> None:
        self.profile = Profile.objects.create(username="test", email="test@test.com", password = "anotehrpasswordtest")
        self.order = Order.objects.create(user=self.profile,paid_amount=float(20000))
    def tearDown(self) -> None:
        return super().tearDown()

    def test_model(self):
        self.assertTrue(isinstance(self.order,Order))
        self.assertEqual(self.order.__str__(), self.order.user.first_name)
        self.assertEqual(self.order.paid_amount,float(self.order.paid_amount) )



class TestOrderItemModel(TestCase):

    def setUp(self) -> None:
        self.profile = Profile.objects.create(username="test", email="test@test.com", password = "anotehrpasswordtest")
        self.order = Order.objects.create(user=self.profile,paid_amount=float(20000))
        self.product = Product.objects.create(created_by=self.profile,price=float(20000))
        self.order_item = OrderItem.objects.create(order=self.order,product=self.product)
    def tearDown(self) -> None:
        return super().tearDown()

    def test_model(self):
        self.assertTrue(isinstance(self.order_item,OrderItem))
        self.assertEqual(self.order_item.__str__(), str(self.order_item.id))
        
        

class TestCreateOrder_View(APITestCase):
    def setUp(self):
        self.profile = Profile.objects.create(username="test", email="test@test.com", password = "anotehrpasswordtest")
        self.token = Token.objects.get(user=self.profile)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.product = Product.objects.create(created_by=self.profile,price=float(20000))
        self.payload = {
            "paid_amount":float(20000),
            "items":[
                {
                    "product":self.product.id
                }
            ]
        }


    def tearDown(self) -> None:
        return super().tearDown()

    def get_url(self):
        return self.client.get(reverse("orders:create_order"))


    def test_url_non_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        res = self.get_url()
        self.assertEqual(res.status_code,401)


    def test_post_method(self):
        res = self.client.post(reverse("orders:create_order"),self.payload,format="json")
        self.assertEqual(res.status_code,201)

  

