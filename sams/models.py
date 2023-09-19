from django.db import models
from django.utils import timezone
# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255)
    vendor_category = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now,blank=True,null=True)
    def __str__ (self):
        return 'el proveedor: %s %s' % (self.vendor_name,self.vendor_category )

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_size = models.CharField(max_length=255,blank=True,null=True)
    product_color = models.CharField(max_length=255,blank=True,null=True)
    product_sku = models.CharField(max_length=255)
    vendor = models.ForeignKey(Vendor,null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now,blank=True,null=True)
    deleted_date = models.DateTimeField(blank=True,null=True)
    def __str__ (self):
        return 'el producto es: %s %s' % (self.product_name,self.product_size )
