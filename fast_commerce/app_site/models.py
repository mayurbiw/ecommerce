# write models here 
from django.db import models 
from django.contrib.auth.models import User


order_status = [
    'placed','shipped','delivered'
]


class Product(models.Model):
    id = models.CharField(max_length=255,primary_key=True)
    name = models.CharField(db_column='Name', max_length=255, verbose_name='Product Name')
    product_code = models.CharField(db_column='ProductCode', max_length=255, blank=True, null=True)
    description = models.TextField(db_column='Description', verbose_name='Product Description', blank=True, null=True)
    is_active = models.BooleanField(db_column='IsActive', verbose_name='Active', default=False)
    family = models.CharField(db_column='Family', max_length=255, verbose_name='Product Family', choices=[('None', 'None')], blank=True, null=True)
    UnitPrice = models.DecimalField(decimal_places=2, max_digits=18)
        
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        # keyPrefix = '01t'

class ReviseOrder(models.Model):
    Product2Id = models.ForeignKey('Product', db_column='Product2Id__c', on_delete=models.DO_NOTHING)    
    user_id = models.ForeignKey(User ,db_column='user_id__c',on_delete=models.DO_NOTHING)
    status = models.CharField(db_column='status__c',choices=[(x, x) for x in order_status],max_length=255)

    class Meta:
        db_table = 'ReviseOrder__c'
        verbose_name = 'ReviseOrder'
        verbose_name_plural = 'ReviseOrders'