import json
from decimal import *
from django.shortcuts import render, HttpResponse
from .models import Item


def view_item(request, item_id):
    item = Item.objects.filter(item_id=item_id)

    if item.exists():
        return HttpResponse(json.dumps(item.first().json()))

    else:
        return HttpResponse("{}")


def search(request):
    name = request.GET.get("name")

    if name is None:
        return HttpResponse("No name")

    # First, do any basic filtering of the items by the item name
    items = Item.objects.filter(name__icontains=name)

    # Since from what I understand DJango can't do dynamic queries easily,
    #   I just do any filtering myself

    price_search_type = request.GET.get("price_search_type")

    if price_search_type is not None:
        price = request.GET.get("price")

        if price is None:
            return HttpResponse("Price required when using price_search_type")


        price = Decimal(price)

        if price < 0.0:
            return HttpResponse("Price must be positive")

        if price_search_type == "lower_than":
            items = filter(lambda item: item.price <= price, items)

        elif price_search_type == "greater_than":
            items = filter(lambda item: item.price >= price, items)

        elif price_search_type == "equal_to":
            items = filter(lambda item: item.price == price, items)

        elif price_search_type == "range":
            low_price = price
            high_price = request.GET.get("high_price")

            if high_price is None:
                return HttpResponse("No high price given")

            high_price = Decimal(high_price)

            items = filter(
                lambda item:
                    item.price >= low_price and item.price <= high_price,
                items
            )

        else:
            return HttpResponse("Bad price search type")

    # Finally, convert each item in the list into a json object,
    #   then convert the iterator into a list
    json_objs = list(map(lambda item: item.json(), items))

    # Finally, convert said list of json objects into a JSON string
    return HttpResponse(json.dumps(json_objs))
