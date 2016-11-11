from django.shortcuts import render
import uuid
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render
from .models import Product

# Create your views here.




def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})