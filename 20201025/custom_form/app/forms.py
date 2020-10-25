from django import forms

class OrderForm(forms.Form):
    qty = forms.IntegerField()
    fullname = forms.CharField()
    phone = forms.CharField()
    address = forms.CharField()