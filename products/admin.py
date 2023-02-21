from django.contrib import admin
from .models import *   # * -> all models


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','old_price','brand','quantity']
    search_fields = ['title',]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title',]


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product','review']
    search_fields = ['product',]


@admin.register(Category)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    search_fields = ['title',]


@admin.register(ProductCategory)
class ProductCategorieAdmin(admin.ModelAdmin):
    list_display = ['product','categorie']
    search_fields = ['product',]


