from django.urls import path
from .views import list_cards, create_card, update_card

app_name = 'cards'

urlpatterns = [
    path('', list_cards, name='list_cards'),
    path('create/', create_card, name='create_card'),
    path('update/<int:pk>', update_card, name='update_card'),
]
