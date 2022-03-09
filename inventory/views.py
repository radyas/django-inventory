from datetime import datetime

import requests
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from inventory.models import Inventory
from inventory.serializers import InventorySerializer, InventoryDetailSerializer
from inventory.utils import format_response_data


class InventoryViewSet(ModelViewSet):
    model = Inventory
    queryset = Inventory.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return InventorySerializer
        else:
            return InventoryDetailSerializer


def inventory(request):
    data = []

    # url to fetch data
    url = f'http://{request.get_host()}/api/inventory'
    response = requests.get(url)

    # set data if the response is successful
    if response.status_code == 200:
        data = format_response_data(response.content)

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
        data = format_response_data(response.content)
        data['added_at'] = datetime.fromisoformat(data['added_at'])

    context = {
        'item': data
    }
    return render(request, 'inventory-detail.html', context)
