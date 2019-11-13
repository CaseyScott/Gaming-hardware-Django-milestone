from django.shortcuts import render
from django.conf import settings


def index(request):
    """A view that displays the index page"""
    context = {
        'EMAIL_JS_KEY': settings.EMAIL_JS_KEY
    }
    return render(request, "index.html", context)
