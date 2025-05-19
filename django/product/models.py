from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100 , verbose_name='العنوان')
    category = models.CharField(max_length=100 , verbose_name='الصنف')
    brand = models.CharField(max_length=100 , verbose_name='الصنف')

    price = models.FloatField(default=0.0, blank=True, null=True , verbose_name='السعر') # unit _ price
    
    created_at = models.DateTimeField(auto_now=True , verbose_name='تاريخ الانشاء') 
