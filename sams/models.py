from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255)
    vendor_category = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    def __str__ (self):
        return 'el proveedor es: %s %s' % (self.vendor_name,self.vendor_category )
