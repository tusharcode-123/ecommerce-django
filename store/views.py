from django.shortcuts import render,get_object_or_404,redirect

from django.contrib import messages
from .models import Product,Category,Reviewrating,ProductGallery
from carts.models import CartItem
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q
from .forms import ReviewForm
from orders.models import OrderProduct
from carts.views import _cart_id

def store(request,category_slug=None):
    categories = None
    product = None
    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        product = Product.objects.filter(category=categories,is_available=True).order_by("-created_date")
        paginator = Paginator(product,1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = product.count()
    else:
        product = Product.objects.all().filter(is_available=True).order_by("-created_date")
        paginator = Paginator(product,3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = product.count()
    context = {
        "products":paged_products,
        "product_count":product_count,
    }
    return render(request,"store/store.html",context)

def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug=product_slug )
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request),product=single_product).exists()
    except Exception as e:
        raise e
    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user,product_id = single_product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None

    reviews = Reviewrating.objects.filter(product_id=single_product.id,status=True)

    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)

    context = {
        "single_product":single_product,
        "in_cart":in_cart,
        "orderproduct":orderproduct,
        "reviews":reviews,
        "product_gallery":product_gallery
    }
    return render(request,'store/product-detail.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            product = Product.objects.order_by("-created_date").filter(Q(description__icontains=keyword) | Q(product_name__icontains = keyword))
            product_count = product.count()
    context = {
        "products":product,
        "product_count":product_count,
    }
    return render(request,"store/store.html",context)


def submit_review(request,product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            reviews = Reviewrating.objects.get(user__id=request.user.id,product__id=product_id)
            form = ReviewForm(request.POST,instance=reviews)
            form.save()
            messages.success(request, 'Thank You? Your review has been updated! ')
            return redirect(url)
        except Reviewrating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = Reviewrating()
                data.subject = form.cleaned_data["subject"]
                data.rating = form.cleaned_data["rating"]
                data.review = form.cleaned_data["review"]
                data.ip = request.META.get("REMOTE_ADDR")
                data.product_id = product_id
                data.user_id = request.user.id 
                data.save()
                messages.success(request, 'Thank You? Your review has been submitted! ')
                return redirect(url)




