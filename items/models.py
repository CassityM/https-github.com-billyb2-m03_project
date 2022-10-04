import json
from django.core import serializers
from django.db import models


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()

    def json(self):
        json_obj = {
            "item_id": self.item_id,
            "name": self.name,
            "price": float(self.price),
            "description": self.description,

        }

        return json_obj

    def __str__(self):
        return self.name
