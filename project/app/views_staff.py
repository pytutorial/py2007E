#app/views_staff.py
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from django.conf import settings
import math

@login_required
def staffHome(request):
    return render(request, 'staff/home.html')

@login_required
def listCategory(request):#127.0.0.1:8000/staff/list-category
    categoryList = Category.objects.all()
    context = {'categoryList' : categoryList}
    return render(request, 'staff/category/list.html', context)

@method_decorator(login_required, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    success_url = '/staff'
    template_name = 'staff/category/form.html'

@method_decorator(login_required, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    success_url = '/staff'
    template_name = 'staff/category/form.html'

@login_required
def deleteCategory(request, pk):
    c = Category.objects.get(pk=pk)
    c.delete()
    return redirect('staff-home')

@login_required
def listProduct(request):
    productList = Product.objects.all()
    context = {'productList': productList}
    return render(request,
        'staff/product/list.html', context)  

@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = '/staff/list-product'
    template_name = 'staff/product/form.html'

@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = '/staff/list-product'
    template_name = 'staff/product/form.html'

@login_required
def deleteProduct(request, pk):
    return redirect('list-product')

@login_required
def listOrder(request):
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1) * pageSize
    end = start + pageSize   
    
    orderList = Order.objects.all()
    orderList = orderList.order_by('status', '-order_date')
    total = orderList.count()
    
    context = {
        'orderList': orderList[start:end],
        'start': start,
        'page': page,
        'total': total,
        'numpage': math.ceil(total/pageSize)
    }
    return render(request, 'staff/order/list.html', context)    

@login_required
def viewOrder(request, pk):
    order = Order.objects.get(pk=pk)    
    context = {'order': order}
    return render(request, 'staff/order/detail.html', context)
    

@login_required
def confirmOrderDeliver(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = Order.Status.DELIVERED
    order.deliver_date = datetime.now()
    order.save()
    return redirect('list-order')

@login_required
def cancelOrder(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = Order.Status.CANCELED
    order.save()
    return redirect('list-order')