from django.conf.urls import url, include
from .views import index


urlpatterns = [
    url(r'^index/', index, name="index"),
]