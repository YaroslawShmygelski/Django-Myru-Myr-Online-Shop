from . import views
from django.urls import path


app_name='shop'
urlpatterns = [
    path('', views.hello_site, name='ap'),
    path("product/<slug:slug>/", views.show_product, name='single-product')]