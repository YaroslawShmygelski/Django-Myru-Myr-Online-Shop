from . import views
from django.urls import path


app_name='shop'
urlpatterns = [
    path('', views.index_view, name='main'),
    path("product/<slug:slug>/", views.show_single_product, name='single-product'),
    path("catalog/", views.show_catalog, name='catalog'),
    path('contact/', views.contact_view, name='contact'),
    path('search-data/', views.get_search_data, name='search-data'),
    path('category/<slug:cat_slug>/', views.get_category_products, name='category')
]