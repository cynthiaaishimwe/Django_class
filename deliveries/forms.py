from django import forms
from .models import Delivery

class Delivery_form(forms.ModelForm):
    class Meta:
        model =  Delivery
        fields = "__all__"