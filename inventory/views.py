from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from inventory.models import Inventory
from inventory.serializers import InventorySerializer, InventoryDetailSerializer
from inventory.utils import get_list_data, get_detail_data


class InventoryViewSet(ModelViewSet):
    model = Inventory
    queryset = Inventory.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return InventorySerializer
        else:
            return InventoryDetailSerializer


def inventory(request):
    # url to fetch data
    url = f'http://{request.get_host()}/api/inventory'

    context = {
        'items': get_list_data(url)
    }
    return render(request, 'inventory.html', context)


def inventory_detail(request, inventory_id):
    # url to fetch data
    url = f'http://{request.get_host()}/api/inventory/{inventory_id}'

    context = {
        'item': get_detail_data(url)
    }
    return render(request, 'inventory-detail.html', context)
