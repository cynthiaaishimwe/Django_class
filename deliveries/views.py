from django.shortcuts import render
from .forms import  Delivery_form

def product_delivery_view(request):
    if request.method == "POST":
        form = Delivery_form(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = Delivery_form()
    return render(request,"Deliveries/deliveries_form.html",{"form":form})  
