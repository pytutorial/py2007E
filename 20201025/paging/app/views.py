from django.shortcuts import render
# Create your views here.
import math
from .models import *
PAGE_SIZE = 10
def index(request):
    name = request.GET.get('name', '')
    productList = Product.objects.filter(name__icontains=name)
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    start = (page-1)* PAGE_SIZE
    end = start + PAGE_SIZE
    total = len(productList)
    num_page = math.ceil(total/PAGE_SIZE)
    context = {
        'page': page,
        'start': start, 'end': end, 
        'total': total, 'num_page': num_page,
        'productList': productList[start:end],
        'name': name
    }
    return render(request, 'index.html', context)
