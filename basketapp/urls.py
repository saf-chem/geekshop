from django.urls import path
from mainapp.views import products
from .views import add, remove


app_name = 'basketapp'

urlpatterns = [
   # path('', basket, name='read'),
    path('add/<int:product_pk>/', add, name='add'),
    path('remove/<int:product_pk>', remove, name='remove'),
    path('edit/<int:pk>/', products, name='edit'),
]