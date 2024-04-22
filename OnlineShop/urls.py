from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
      path("Shop_Main/",views.Shop_Main, name="Shop_Main"),
      path('add-to-cart/<str:name>/', views.add_to_cart, name='add_to_cart'),
      path('remove-from-cart', views.remove_from_cart, name='remove_from_cart'),
      path('cart/', views.cart, name='cart'),
      path('checkout/', views.checkout, name='checkout'),
      path('request-refund/', views.request_refund, name='request_refund'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

