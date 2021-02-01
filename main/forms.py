from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get("age")
        if age < 18:            
            raise ValidationError(
                "Your age is too small"
            )

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
