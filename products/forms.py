from django import forms
from products.models import Product


class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
        }


class EditProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
