from django.shortcuts import render, redirect
from .models import Product

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        location = request.POST.get('location')
        Product.objects.create(name=name, price=price, location=location)
        return redirect('add me')
    return render(request, 'add.html')

def view(request):
    products = Product.objects.all()
    return render(request, 'view.html', {'products': products})

def delete(request,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    return redirect('view')

    