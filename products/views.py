from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product


class ItemDetailView(DetailView):
    model = Product

def all_products(request, requestedCategory):
    products = Product.objects.filter(category=requestedCategory)
    return render(request, "products.html", {"products": products})
