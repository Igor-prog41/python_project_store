from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Customer(models.Model):
    first_name = models.CharField(max_length=200, null=False, blank=False, verbose_name="First name")
    last_name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Last name")
    phone = models.BigIntegerField(unique=True, null=False, blank=False, verbose_name="Phone")
    email = models.CharField(max_length=200, unique=True, null=False, blank=False, verbose_name="email")
    time_created = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    token = models.CharField(max_length=300,null=False, blank=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    def __str__(self):
        return self.first_name


class CustomerAddress(models.Model): 
    city = models.CharField(max_length=100,null=False,blank=False,verbose_name="City")
    post_code = models.IntegerField(default=0,null=False,blank=False,verbose_name="Post code")
    address = models.CharField(max_length=200,null=False,blank=False,verbose_name="Address")
    customer = models.ForeignKey('customers.Customer',null=True,blank=True,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'customer_address'
        verbose_name = 'Customer Address'
        verbose_name_plural = 'Customers Addresses'
    def __str__(self):
        return self.address
