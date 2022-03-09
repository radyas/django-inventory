from rest_framework import serializers

from inventory.models import Inventory, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    supplier = serializers.CharField(source='supplier.name', default='N/A')

    class Meta:
        model = Inventory
        fields = ['id', 'name', 'availability', 'supplier']


class InventoryDetailSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    added_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    added_by = serializers.CharField(source='added_by.get_full_name', default='admin')

    class Meta:
        model = Inventory
        fields = '__all__'
