#app/views_staff.py
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView

def staffHome(request):
    return render(request, 'staff/home.html')

def listCategory(request):#127.0.0.1:8000/staff/list-category
    categoryList = Category.objects.all()
    context = {'categoryList' : categoryList}
    return render(request, 'staff/category/list.html', context)

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    success_url = '/staff/list-category'
    template_name = 'staff/category/form.html'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    success_url = '/staff/list-category'
    template_name = 'staff/category/form.html'

def deleteCategory(request, pk):
    c = Category.objects.get(pk=pk)
    c.delete()
    return redirect('list-category')

def listProduct(request):
    productList = Product.objects.all()
    context = {'productList': productList}
    return render(request,
        'staff/product/list.html', context)  

def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    return render(request, 'staff/product/form.html',
                {'form': form})

def updateProduct(request, pk):
    return render(request, 'staff/product/form.html')

def deleteProduct(request, pk):
    return redirect('list-product')