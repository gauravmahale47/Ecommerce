from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from webapp.forms import ProductForm
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.detail import DetailView


def home(request):
    return render(request,'webapp/home.html')

def addproduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productlist')
    data = {'form':form}
    return render(request, 'webapp/add.html', data)

class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'webapp/productlist.html'

class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('productlist')

class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    success_url=reverse_lazy('productlist')

class ProductDetail(DetailView):
    model = Product
    template_name='webapp/detail.html'

class Clothing(ListView):
    model = Product
    context_object_name = 'list'
    template_name = 'webapp/clothing.html'

class Watches(ListView):
    model = Product
    context_object_name = 'list'
    template_name = 'webapp/watches.html'