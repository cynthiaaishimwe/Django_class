
from django import forms
from .models import Locations

class LocationDisplayForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"