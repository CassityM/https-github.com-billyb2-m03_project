from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('view_item/<int:item_id>', views.view_item, name='view_item'),
]
