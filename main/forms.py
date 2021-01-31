from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()

    class Meta:
        model = User
        fields = [
            "firstname",
            "lastname",
            "email",
            "address",
        ]  # list of fields you want from model
