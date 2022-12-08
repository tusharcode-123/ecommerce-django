from django.urls import path,include
from . import views
urlpatterns = [ 
    path("",views.store,name="Store"),  
    path("category/<slug:category_slug>/",views.store,name="Product_by_category"),
    path("category/<slug:category_slug>/<slug:product_slug>/",views.product_detail,name="Product_Detail"),
    path("search/",views.search,name="Search"),
] 