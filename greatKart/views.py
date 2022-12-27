from django.shortcuts import render
from store.models import Product
from store.models import Reviewrating

def home(request):
    product = Product.objects.all().filter(is_available=True).order_by("created_date")
    for p in product:
        reviews = Reviewrating.objects.filter(product_id=p.id,status=True)
    context = {
        "products":product,
        "reviews":reviews
    }
    return render(request,"home.html",context)