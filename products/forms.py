from django import forms
from products.models import Product


class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class EditProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
