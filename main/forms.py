from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

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
