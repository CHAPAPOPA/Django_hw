from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home_page, contact_information, products_list, specific_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='products'),
    path('product/<int:pk>/', specific_product, name='specific_product'),
    path('home/', home_page, name='home'),
    path('contacts/', contact_information, name='contact')
]
