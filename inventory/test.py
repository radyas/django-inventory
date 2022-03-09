import json
from unittest.mock import patch

from django.test import TestCase, Client

from django.contrib.auth.models import User
from rest_framework.test import APIClient

from inventory.models import Inventory, Supplier


class MockListResponse:
    def __init__(self):
        self.status_code = 200

    def json(self):
        return json.dumps([
            {
                "id": 1,
                "name": "Product 1",
                "availability": True,
                "supplier": "Supplier 1"
            },
            {
                "id": 2,
                "name": "Product 2",
                "availability": True,
                "supplier": "Supplier 1"
            }
        ])


class MockDetailResponse:
    def __init__(self):
        self.status_code = 200

    def json(self):
        return json.dumps({
            "id": 2,
            "supplier": {
                "id": 3,
                "name": "Supplier 1",
                "address": "Supplier 1 Address",
                "phone": 712755777
            },
            "added_at": "2022-03-09 17:58:15",
            "added_by": "",
            "name": "Product 2",
            "description": "Test Product",
            "note": "New Product",
            "stock": 12,
            "availability": True,
            "updated_at": "2022-03-09T17:58:15.522361Z"
        })


class SupplierCreationTestCase(TestCase):
    def setUp(self):
        Supplier.objects.create(name="Supplier 1", address="Supplier 1 Address", phone='0712755777')
        Supplier.objects.create(name="Supplier 2", address="Supplier 2 Address", phone='0767769769')

    def test_supplier_creation(self):
        suppliers = Supplier.objects.all()

        self.assertEqual(suppliers.count(), 2)


class UserCreationTestCase(TestCase):
    def setUp(self):
        User.objects.create(first_name="Admin", last_name="One", username='admin', email='admin@admin.com')
        User.objects.create(first_name="Admin", last_name="Two", username='admin2', email='admin2@admin.com')

    def test_user_creation(self):
        users = User.objects.all()

        self.assertEqual(users.count(), 2)


class InventoryCreationTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(first_name="Admin", last_name="One", username='admin', email='admin@admin.com')
        supplier = Supplier.objects.create(name="Supplier 1", address="Supplier 1 Address", phone='0712755777')
        Inventory.objects.create(name="Product 1", stock=25, supplier=supplier, added_by=user)
        Inventory.objects.create(
            name="Product 2", stock=12, supplier=supplier, added_by=user, description='Test Product', note='New Product'
        )

    def test_inventory_creation(self):
        inventory = Inventory.objects.all()

        self.assertEqual(inventory.count(), 2)
        self.assertEqual(inventory.first().added_by.get_full_name(), 'Admin One')
        self.assertEqual(inventory.first().supplier.name, 'Supplier 1')

    def test_inventory_list_endpoint(self):
        client = APIClient()

        response = client.get('/api/inventory/')
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_endpoint(self):
        client = APIClient()
        inventory = Inventory.objects.first()
        response = client.get(f'/api/inventory/{inventory.pk}/')
        self.assertEqual(response.status_code, 200)

    @patch("requests.get", return_value=MockListResponse())
    def test_inventory_template(self, mocked):
        client = Client()

        response = client.get('/inventory')
        self.assertEqual(response.status_code, 200)

    @patch("requests.get", return_value=MockDetailResponse())
    def test_inventory_detail_template(self, mocked):
        client = Client()

        inventory = Inventory.objects.first()
        response = client.get(f'/inventory/{inventory.pk}')
        self.assertEqual(response.status_code, 200)
