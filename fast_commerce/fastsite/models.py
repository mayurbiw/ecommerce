# write models here 
from django.db import models 


"""
class Product(models.Model):
    name = models.CharField(db_column='Name', max_length=255, verbose_name='Product Name')
    product_code = models.CharField(db_column='ProductCode', max_length=255, blank=True, null=True)
    description = models.TextField(db_column='Description', verbose_name='Product Description', blank=True, null=True)
    is_active = models.BooleanField(db_column='IsActive', verbose_name='Active', default=False)
    family = models.CharField(db_column='Family', max_length=255, verbose_name='Product Family', choices=[('None', 'None')], blank=True, null=True)
    
    class Meta:
        db_table = 'Product2'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        # keyPrefix = '01t'
"""