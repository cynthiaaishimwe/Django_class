from django.shortcuts import render
from .forms import ContactDisplay

def contact_upload_view(request):
    if request.method == "POST":
        form = ContactDisplay(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ContactDisplay()
    return render(request,"contacts/contact_upload.html",{"form":form})  
