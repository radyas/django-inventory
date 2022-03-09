from django.contrib.auth.models import User
from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    phone = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Inventory(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True)
    note = models.TextField(null=True)
    stock = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, related_name='added_inventory', on_delete=models.SET_NULL, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.name
