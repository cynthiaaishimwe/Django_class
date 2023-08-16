from django.shortcuts import render
from .forms import Vendor_form
from .models import Vendor
from django.shortcuts import render,redirect

def vendor_upload_view(request):
    if request.method == "POST":
        form = Vendor_form(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = Vendor_form()
    return render(request,"vendors/vendor_form.html",{"form":form})
    


def vendor_display(request):
    vendors = Vendor.objects.all()
    return render(request,"vendors/vendor_display.html",{"vendors":vendors})


def vendor_detail(request,id):
    vendor= Vendor.objects.get(id=id)
    return render(request,"vendors/vendor_detail.html",{"vendors":vendor})