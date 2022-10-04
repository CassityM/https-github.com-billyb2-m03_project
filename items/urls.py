from django.urls import path
from . import views

urlpatterns = [
    path('view_item/<int:item_id>', views.view_item, name='view_item'),
    path("search", views.search, name="search"),
]
