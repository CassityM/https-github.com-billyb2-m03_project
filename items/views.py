import json
from django.shortcuts import render, HttpResponse
from .models import Item


def view_item(request, item_id):
    item = Item.objects.filter(item_id=item_id)

    if item.exists():
        return HttpResponse(item.first().json())

    else:
        return HttpResponse("{}")
