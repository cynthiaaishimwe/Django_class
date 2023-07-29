from django.db import models
from basket.models import Basket
from customers.models import Customer
from shipment.models import Shipment

class Orders(models.Model):
    purchaser_name=models.CharField(max_length=32)
    purchaser_number=models.CharField(max_length=32)
    vendor_name=models.CharField(max_length=32)
    vender_number=models.CharField(max_length=32)
    product_description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=6)
    quantity=models.PositiveIntegerField()
    lbasket =models.ForeignKey(Basket,null=True,on_delete=models.CASCADE)
    customers = models.OneToOneField(Customer, null =True, on_delete = models.CASCADE)
    shipment = models.ManyToManyField(Shipment,null =True ,blank = True)


def __str__(self):
    return self.purchaser_number



# def product_upload_view(request):
#     if request.method == "POST":
#         form  = productUploadForm(request.POST)
#         if  form.isValid():
#             form.save()
#     else:
#         form = ProductUploadForm()
#     return54 render(request,inventory/product_upload.html)
#             {"form": form})
    

# for product in product:
#    print(product.title):
#    print(product.name):
    # print(product.name):