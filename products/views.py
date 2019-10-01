from django.shortcuts import render,HttpResponse
from .models import Products
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
    products = Products.objects.all()[:4]
    return render(request,'products/index.html',context={'products':products})
def add_product(request):
    return render(request,'products/add_product.html')
def products(request):
    products = Products.objects.all
    return render(request,'products/products.html',context={'products':products})
class ProductDetailView(DetailView):
    model = Products