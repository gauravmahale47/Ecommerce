from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',home, name="home"),
    path('addproduct',addproduct, name="addproduct"),
    path('productlist',ProductList.as_view(),name='productlist'),
    path('edit/<pk>',UpdateProduct.as_view(),name='edit'),
    path('delete/<pk>',DeleteProduct.as_view(),name='delete'),
    path('clothing',Clothing.as_view(),name='clothing'),
    path('watches',Watches.as_view(),name='watches'),
    path('detail/<pk>',ProductDetail.as_view(),name='detail')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)