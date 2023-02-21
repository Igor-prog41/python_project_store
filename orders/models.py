from django.db import models
from products.models import Product
from customers.models import Customer

class Order(models.Model):
    time_created = models.DateTimeField(auto_created=True)
    time_checkout = models.DateTimeField(null=True, blank=True)
    time_delivery = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey('customers.Customer',null=False,blank=False,on_delete=models.CASCADE)
    customer_shipping_address = models.ForeignKey('customers.CustomerAddress',null=True,blank=True,on_delete=models.SET_NULL)
    is_ordered = models.BooleanField(default=False)
    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    def __str__(self):
        return self.customer.first_name


class OrderProduct(models.Model):
    order = models.ForeignKey('orders.Order',null=False,blank=False,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=False,blank=False,on_delete=models.CASCADE)
    price = models.DecimalField(default=0,max_digits=9,decimal_places=2,null=False,blank=False)
    quantity =models.IntegerField(default=0,null=False,blank=False)
    class Meta:
        db_table = 'order_product'
        verbose_name = 'Order Product'
        verbose_name_plural = 'Orders Products'
    def __str__(self):
        return str(self.order)+" - " + str(self.product)
