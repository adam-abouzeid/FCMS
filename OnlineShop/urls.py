from django.urls import path
from . import views

urlpatterns = [
      path("FanShop", views.Shop_Main, name="Shop_Main"),
      path('product/<int:product_id>/', views.product_list, name='product_list'),
      path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
      path('remove-from-cart/<int:order_item_id>/', views.remove_from_cart, name='remove_from_cart'),
      path('cart/', views.cart, name='cart'),
      path('checkout/', views.checkout, name='checkout'),
      path('request-refund/', views.request_refund, name='request_refund'),

]