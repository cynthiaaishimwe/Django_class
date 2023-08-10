from django.shortcuts import render
from .forms import LocationDisplayForm

def location_upload_view(request):
    if request.method == "POST":
        form = LocationDisplayForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = LocationDisplayForm()
    return render(request,"Location/location_upload.html",{"form":form})    
    

def location_update_view(request,id):
    location = location.objects.get(id=id)
    if request.method == "POST":
       form =LocationDisplayForm(request.POST,instance=location)
       if form.is_valid():
          form.save()
       return redirect("location_upload_view",id =location.id)
    else:
        form = LocationDisplayForm(instance=product)
        return render(request,"location/edit_location.html",{"form":form})     