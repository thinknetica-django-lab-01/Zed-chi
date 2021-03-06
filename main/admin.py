from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from .models import Product, Seller, ProductCategory, ProductImage, Tag, Subscriber


class FlatPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FlatPage
        fields = "__all__"


FlatPageAdmin.form = FlatPageAdminForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)
admin.site.register(Tag)
admin.site.register(Subscriber)
