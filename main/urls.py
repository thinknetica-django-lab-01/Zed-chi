from django.contrib.flatpages import views
from django.urls import path

from .views import homepage, ProductsListView, ProductDetailView

app_name = "main"
urlpatterns = [
    path("", homepage, name="homepage"),
    path("about/", views.flatpage, {"url": "/about/"}, name="about"),
    path("contacts/", views.flatpage, {"url": "/contacts/"}, name="contacts"),
    path("goods", ProductsListView.as_view(), name="goods_list"),
    path("goods/<int:pk>", ProductDetailView.as_view(), name="good_detail"),
]
