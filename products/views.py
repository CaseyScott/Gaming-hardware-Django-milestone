from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product


class ItemDetailView(DetailView):
    model = Product


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def video_cards(request):
    videoCards = Product.objects.video_cards()
    return render(request, "videoCard.html", {"videoCards": videoCards})
