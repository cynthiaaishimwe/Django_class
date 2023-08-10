from django.shortcuts import render
from .forms import CustomerDisplayForm


def customer_upload_view(request):
    if request.method == "POST":
        form = CustomerDisplayForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CustomerDisplayForm()
    return render(request,"customers/customer_upload.html",{"form":form})  
