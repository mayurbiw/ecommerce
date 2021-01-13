from django.shortcuts import render
from . salesforce_models import Product, PricebookEntry, Pricebook
# Create your views here.
def index(request):
    standard_price_book = Pricebook.objects.get(Name="Standard Price Book")
    products = PricebookEntry.objects.all().select_related('Product2').select_related('Pricebook2').filter(Pricebook2=standard_price_book)
    
    return render(request,"fastsite/index.html",dict(tittle="All products",products = products))


def list_products(request):
    standard_price_book = Pricebook.objects.get(Name="Standard Price Book")
    products = PricebookEntry.objects.all().select_related('Product2').select_related('Pricebook2').filter(Pricebook2=standard_price_book)
    
    """
    for p in products:
        pe = pricebook_entries.filter(Product2=p)
        print(p.Name)
        print("prices")
        for entry in pe:
            print("price = "+ str(entry.UnitPrice)) 
    """
    return render(request,'fastsite/list-products.html',dict(tittle="All products",products = products))



