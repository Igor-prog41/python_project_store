from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['time_created','time_checkout','time_delivery','customer','is_ordered']
    search_fields = ['customer',]


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['order','product','price','quantity']
    search_fields = ['order',]