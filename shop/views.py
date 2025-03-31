from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


def shop(request):
    return render(request, 'shop/shop.html')


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
