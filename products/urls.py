from django.conf.urls import url, include
from .views import all_products, ItemDetailView, video_cards


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item_detail'),
    url(r'^$', video_cards, name='videoCards'),
]
