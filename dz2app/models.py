from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=128)
    date_registered = models.DateTimeField(auto_now_add=True)
    def __char__(self):
        return (f'Id Client: {id}, Username: {self.client}, email: {self.email}, phone: {self.phone}, '
                f'address: {self.address}')


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=128)
    description = models.TextField()
    price = models
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.__str__()