from django.urls import path
from .views import checkout_session, item_detail, item

urlpatterns = [
    path('buy/<int:id>/', checkout_session, name='checkout_session'),
    path('item_detail/<int:id>/', item_detail, name='item_detail'),
    path('item/<int:item_id>/', item, name='item'),
]
