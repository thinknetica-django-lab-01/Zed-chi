from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Seller, Product


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get("age")
        if age < 18:
            raise ValidationError("Your age is too small")

    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    age = forms.IntegerField(min_value=18, max_value=150)

    class Meta:
        model = User
        fields = [
            "firstname",
            "lastname",
            "email",
            "address",
            "age",
        ]


class GoodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = forms.CharField(label="Название")
    description = forms.CharField(widget=forms.Textarea, label="Описание")
    price = forms.IntegerField(label="Цена")
    seller = forms.ModelMultipleChoiceField(
        queryset=Seller.objects.all(),
        label="Продавец",
    )

    class Meta:
        model = Product
        fields = ["name", "description", "price", "seller"]
