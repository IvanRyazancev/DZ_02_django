from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm
from .models import Client, Product, Order, OrderItem
import datetime

def create_client(name, email, phone, address):
    client = Client(client=name, email=email, phone=phone, address=address)
    client.save()
    return client

def add_product(name, description, price, quantity):
    product = Product(product=name, description=description, price=price, quantity=quantity)
    product.save()
    return product

def create_order(client_id, product_quantities):
    order = Order(client_id=client_id)
    order.save()
    for product_id, quantity in product_quantities.items():
        OrderItem(order=order, product_id=product_id, quantity=quantity).save()
    return order

def get_order_total(order_id):
    order = Order.objects.get(id=order_id)
    return order.get_total_cost()

def client_product(request, user_id, days):
    user = get_object_or_404(Client, id=user_id)
    orders = Client.objects.filter(customer=user, date_ordered__gte=timezone.now() - datetime.timedelta(days=days))
    products = set()

    for order in orders:
        products.update(order.products.all())

    context = {'user': user, 'days': days, 'products': products}
    return render(request, 'dz2app/client_product.html', context)

def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                amount=form.cleaned_data['amount'],
                photo=form.cleaned_data['photo']
            )
            product.save()
    else:
        form = ProductForm()
    products = Product.objects.all()
    context = {
        "title": "Продукты",
        "products": products,
        'form': form,
    }
    return render(request, 'dz2app/product.html', context)