from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=128)
    date_registered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (f'Id Client: {self.id}, Username: {self.client}, email: {self.email}, phone: {self.phone}, '
                f'address: {self.address}')


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    # photo = models.ImageField()
    def __str__(self):
        return f'Product #{self.id}: {self.product}, price: {self.price}, quantity: {self.quantity}'

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def str(self):
        return f'{self.quantity} x {self.product.product}'

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    date_ordered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Order {self.id} by {self.client.client}'
    def get_total_cost(self):
        return sum(item.quantity * item.product.price for item in self.orderitem_set.all())
