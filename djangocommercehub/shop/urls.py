from django.urls import path
from .views import get_checkout_session, item_detail

urlpatterns = [
    path('buy/<int:id>/', get_checkout_session, name='get_checkout_session'),
    path('item/<int:id>/', item_detail, name='item_detail'),
]
