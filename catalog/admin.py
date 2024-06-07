from django.contrib import admin
from django.utils.safestring import mark_safe

from catalog.models import Category, Product, Version


class DataMixin:
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(DataMixin, admin.ModelAdmin):
    fields = ['name', 'slug', 'description', 'image', 'category', 'purchase_price',
              'is_published', 'user', 'views_counter', ]
    list_display = ("id", "name", "category", "purchase_price")
    list_filter = ("category",)
    search_fields = ("name",)
    readonly_fields = ('image', 'user', 'views_counter',)

    @admin.display(description='Картинка')
    def post_image(self, product: Product):
        if product.image:
            return mark_safe(f"<img src='{product.image.url}'>")
        return 'Нет картинки'


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "number", "name", "is_active")
    list_filter = ("product", "is_active")
    search_fields = ("name",)
