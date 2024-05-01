from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home_page, contact_information

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name='home'),
    path('contacts/', contact_information, name='contact')
]
