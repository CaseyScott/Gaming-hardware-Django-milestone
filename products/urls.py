from django.conf.urls import url, include
from .views import all_products, ItemDetailView, filter_products


urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^(?P<requestedCategory>[a-zA-Z ]*)$', filter_products, name='filter_products'),

    # This url is for readmore page on each item
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item_detail'),
]
