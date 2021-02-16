from django import forms
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from allauth.account.adapter import get_adapter

from .models import Seller, Product
from allauth.account.utils import (    
    setup_user_email,    
)


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


class UserSignUpForm(SignupForm):
    class Meta:
        model = User
    def save(self, request):        
        adapter = get_adapter(request)
        user = adapter.new_user(request)                        
        group = Group.objects.get(name="CommonUsers")        
        adapter.save_user(request, user, self)
        group.user_set.add(user)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])       
        return user
