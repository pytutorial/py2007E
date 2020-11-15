from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from .forms import *

priceList = [
    {'id': 1, 'name': 'Dưới 5 triệu', 'max': 5},
    {'id': 2, 'name': 'Từ 5 đến triệu', 'min': 5, 'max': 10},
    {'id': 3, 'name': 'Trên 10 triệu', 'min': 10},
]

def index(request):
    name = request.GET.get('name', '')
    categoryId = request.GET.get('categoryId')    
    productList = Product.objects.filter(name__icontains=name)    
    categoryId = int(categoryId) if categoryId else None
    if categoryId:
        productList = productList.filter(category__id=categoryId)
    
    priceId = request.GET.get('priceId')
    priceId = int(priceId) if priceId else None
    price = priceList[priceId-1] if priceId else {}
    minPrice, maxPrice = price.get('min'), price.get('max')
    print(price)
    if minPrice: 
        productList = productList.filter(price__gte=minPrice)

    if maxPrice:
        productList = productList.filter(price__lte=maxPrice)
            
    categoryList = Category.objects.all()
    context = {
        'priceList': priceList,
        'categoryList': categoryList,
        'productList': productList,
        'name': name,
        'categoryId': categoryId,
        'priceId': priceId,
    }
    return render(request, 'index.html', context)

def viewProductDetail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context)

def orderProduct(request, pk):
    product = Product.objects.get(pk=pk)
    form = OrderForm(initial={'qty': 1})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Order()
            order.product = product
            order.qty = data['qty']
            order.customer_name = data['customer_name']
            order.customer_phone = data['customer_phone']
            order.customer_address = data['customer_address']
            order.order_date = datetime.now()
            order.status = Order.Status.NEW
            order.save()
            return redirect('/thank-you')

    context = {'form': form, 'product': product}
    return render(request, 'order.html', context)

def thank_you(request):
    return render(request, 'thank_you.html')