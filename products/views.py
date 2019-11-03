from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def filter_products(request, requestedCategory):
    products = Product.objects.filter(category=requestedCategory)
    return render(request, "products.html", {"products": products})

class ItemDetailView(DetailView):
    model = Product
