from django.urls import path
from . import views
from .views import client_product

urlpatterns = [
    path('user/<int:user_id>/<int:days>', client_product, name='client_product'),
    path('product/', views.product, name='product'),
]