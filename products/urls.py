from django.urls import path,include
from .import views
from django.views import generic
urlpatterns=[
    path('index',views.index,name='index'),
    path('add_product',views.add_product,name='add_product'),
    path('products',views.products,name='products'),
    path('Products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]