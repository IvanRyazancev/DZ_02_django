from django.contrib import admin
from .models import Client, Product, Order

# Register your models here.
from django.contrib import admin
from .models import Client, Product, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client', 'email', 'phone', 'date_registered']
    list_filter = ['client', 'date_registered']
    search_fields = ['client', 'email']
    search_help_text = 'Поиск по полям Имя(Name) и Email'
    list_editable = ['phone']

    readonly_fields = ['email']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'quantity', 'date_added']
    list_filter = ['product', 'date_added']
    search_fields = ['product', 'description']
    search_help_text = 'Поиск по полям Имя(Name) и Описание(Description)'
    list_editable = ['quantity', 'price']

    # readonly_fields = ['photo']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'date_ordered']
    list_filter = ['client', 'date_ordered']
    search_fields = ['client']
    search_help_text = 'Поиск по полю Покупатель(client)'