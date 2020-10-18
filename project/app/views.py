from django.shortcuts import render

from .models import *

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
            
    categoryList = Category.objects.all()
    context = {
        'priceList': priceList,
        'categoryList': categoryList,
        'productList': productList,
        'name': name,
        'categoryId': categoryId,
    }
    return render(request, 'index.html', context)

def viewProductDetail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context)