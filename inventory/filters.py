from django_filters import rest_framework as filters

from inventory.models import Inventory


class InventoryFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Inventory
        fields = ['name', 'availability', 'supplier']
