from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email','time_created','user']
    search_fields = ['first_name',]


@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['city','post_code','address','customer']
    search_fields = ['customer',]
