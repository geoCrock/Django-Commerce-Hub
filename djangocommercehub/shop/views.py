from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
import stripe
from .models import Item

import os
from dotenv import load_dotenv

# Import environment
load_dotenv()

STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY')
stripe.api_key = STRIPE_API_KEY


@require_GET
@csrf_exempt
def get_checkout_session(request, id):
    item = get_object_or_404(Item, id=id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(item.get_absolute_url()),
        cancel_url=request.build_absolute_uri(item.get_absolute_url()),
    )

    return JsonResponse({'session_id': session.id})


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return JsonResponse({'name': item.name, 'description': item.description, 'price': str(item.price)})


def item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {'item': item}
    return render(request, 'item_detail.html', context)
