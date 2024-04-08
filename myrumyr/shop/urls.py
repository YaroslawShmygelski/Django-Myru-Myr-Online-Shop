from . import views
from django.urls import path


app_name='shop'
urlpatterns = [
    path('', views.index_view, name='main'),
    path("product/<slug:slug>/", views.show_single_product, name='single-product'),
    path("catalog/", views.show_catalog, name='catalog'),
    path("cart/", views.cart_view, name='cart')
]