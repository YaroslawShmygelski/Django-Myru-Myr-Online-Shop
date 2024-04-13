from . import views
from django.urls import path

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add-product/<slug:slug>/', views.add_to_cart, name='add_to_cart')
]