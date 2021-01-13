from celery import shared_task 
import app_site.models  as local_db
import fastsite.salesforce_models as sf
import json

@shared_task
def sync_products():
    """
    for now only from sales force to local db.
    """
    sf_products_queryset =  sf.Product.objects.all()
    local_products_queryset =  local_db.Product.objects.all()

    ids=[]
    [ids.append(x.id) for x in local_products_queryset]

    products_to_add = sf_products_queryset.exclude(id__in=ids)

    print("Number of products to add")
    print(len(products_to_add))
    
    if len(products_to_add) > 0 :
        standard_price_book = sf.Pricebook.objects.get(Name="Standard Price Book")
        for product in products_to_add:
            print("Adding "+str(product))
            try:
                price_entry =sf.PricebookEntry.objects.filter(Product2=product,Pricebook2=standard_price_book).values('UnitPrice').get()['UnitPrice']
            except:
                price_entry = 0 
            
            p = local_db.Product(id=product.id,name=product.name,product_code=product.product_code,description=product.description,is_active=product.is_active,family=product.family,UnitPrice=price_entry)
            p.save()



    
    



