from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    pk = models.AutoField(primary_key=True)
    client = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=128)
    date_registered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (f'Id Client: {self.pk}, Username: {self.client}, email: {self.email}, phone: {self.phone}, '
                f'address: {self.address}')


class Product(models.Model):
    pk = models.AutoField(primary_key=True)
    product = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Product #{self.pk}: {self.product}, price: {self.price}, amount: {self.quantity}'

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        products = ', '.join([product.product for product in self.products.all()])
        return (f'Order #{self.pk}: customer: {self.customer.client}, total_price: {self.total_price}, '
                f'products: {products}')