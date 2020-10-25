from django.shortcuts import render
from .forms import OrderForm
def index(request):
    form = OrderForm(initial={'qty': 1})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print('data=', data)
    context = {'form': form}
    return render(request, 'index.html', context)
