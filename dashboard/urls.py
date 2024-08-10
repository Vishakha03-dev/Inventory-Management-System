from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', index, name='index'),
    path('staff/', staff, name='staff'),
    path('staff/details/<int:pk>/', staff_detail, name='staff-detail'),
    path('product/', product, name='product'),
    path('order/', order, name='order'),
    path('product/delete/<int:pk>/', product_delete, name='product-delete'),
    path('product/update/<int:pk>/', product_update, name='product-update'),
]
