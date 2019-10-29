from django.conf.urls import url, include
from .views import all_products, ItemDetailView, video_cards


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item_detail'),

    url(r'^$', video_cards, name='videoCards'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='video_card_detail'),
]

# from django.conf.urls import url, include
# from .views import (
#     video_cards_page,
#     video_cards_detail
# )

# urlpatterns = [
#     url(r'^$', video_cards_page, name='video-cards-products'),
#     url(r'^(?P<pk>\d+)/$', video_cards_detail, name='video-card-detail')
# ]