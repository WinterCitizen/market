from django.urls import path
from orders.views import add_to_card, CardDetailView


urlpatterns = [
    path(
        'add/<int:door>/<int:picture>/',
        add_to_card,
        name='add_to_card'),
    path(
        'detail/',
        CardDetailView,
        name='card_detail',
    )
]
