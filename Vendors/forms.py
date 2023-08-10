from django import forms
from .models import Vendor

class Vendor_form(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__"