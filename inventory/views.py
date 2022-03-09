import requests
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from inventory.models import Inventory


class InventoryViewSet(ModelViewSet):
    model = Inventory


def inventory(request):
    data = []

    # url to fetch data
    url = f'http://{request.get_host()}/api/inventory'
    response = requests.get(url)

    # set data if the response is successful
    if response.status_code == 200:
        data = response.content

    context = {
        'items': data
    }
    return render(request, 'inventory.html', context)


def inventory_detail(request, inventory_id):
    data = None

    # url to fetch data
    url = f'http://{request.get_host()}/api/inventory/{inventory_id}'
    response = requests.get(url)

    # set data if the response is successful
    if response.status_code == 200:
        data = response.content

    context = {
        'item': data
    }
    return render(request, 'inventory-detail.html', context)
