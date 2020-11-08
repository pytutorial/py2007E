#app/views_staff.py
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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

@login_required
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    return render(request, 'staff/product/form.html',
                {'form': form})

@login_required
def updateProduct(request, pk):
    return render(request, 'staff/product/form.html')

@login_required
def deleteProduct(request, pk):
    return redirect('list-product')