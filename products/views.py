from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product


def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)  # Show 6 products per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, "products.html", {"products": products})


def filter_products(request, requestedCategory):
    products = Product.objects.filter(category=requestedCategory)
    paginator = Paginator(products, 6)  # Show 6 products per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results.
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})


class ItemDetailView(DetailView):
    model = Product
