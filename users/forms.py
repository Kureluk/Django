from django import forms
from users.models import Users


class CreateUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"


class EditUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"



