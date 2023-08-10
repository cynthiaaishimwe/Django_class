
from django.shortcuts import render
from .forms import Vendor_form

def  Vendor_form_view(request):
    if request.method == "POST":
        form =  Vendor_form(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = Vendor_form()
    return render(request,"vendors/vendor_upload.html",{"form":form})  


