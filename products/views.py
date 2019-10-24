from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

class ItemDetailView(DetailView):
    model = Product


def video_cards(request):
    videoCards = Product.objects.all()
    return render(request, "videoCards.html", {"videoCards": videoCards})

class ItemVideoCardDetailView(DetailView):
    model = Product
