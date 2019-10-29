from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product


class ItemDetailView(DetailView):
    model = Product


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def video_cards(request):
    video_cards = Product.objects.video_cards()
    return render(request, "videoCard.html", {"video_cards": video_cards})

# from django.shortcuts import render, get_object_or_404

# from .models import Product


# Render only video cards
# def video_cards_page(request):
#     qs = Product.objects.video_cards()
#     template_name = "video_cards/video_cards.html"
#     context = {"hardware_products": qs}
#     return render(request, template_name, context)

# def video_cards_detail(request, slug):
#     qs = get_object_or_404(Product, slug=slug)
#     template_name = "video_cards/video_cards_detail.html"
#     context = {"video_cards_detail": qs}
#     return render(request, template_name, context)
