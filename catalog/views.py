from django.http import HttpResponseRedirect

import csv

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.models import Product


class HomePageView(TemplateView):
    template_name = 'catalog/home_page.html'


class ContactInformationView(TemplateView):
    template_name = 'catalog/contact_information.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        with open('contact_info.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, message])

        return HttpResponseRedirect(self.request.path)


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'purchase_price', 'image')
    success_url = reverse_lazy('catalog:products')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'purchase_price', 'image')
    success_url = reverse_lazy('catalog:products')

    def get_success_url(self):
        return reverse_lazy('catalog:specific_product', args=[self.kwargs['pk']])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')
