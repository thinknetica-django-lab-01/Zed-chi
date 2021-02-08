from django.contrib.flatpages import views
from django.urls import path

from .views import (
    HomepageView,
    ProductsListView,
    ProductDetailView,
    ProfileView,
    AddGoodView,
    GoodUpdateView,
)

app_name = "main"
urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path("about/", views.flatpage, {"url": "/about/"}, name="about"),
    path("contacts/", views.flatpage, {"url": "/contacts/"}, name="contacts"),
    path("goods", ProductsListView.as_view(), name="goods_list"),
    path("goods/add", AddGoodView.as_view(), name="add_good"),
    path("goods/<int:pk>/edit", GoodUpdateView.as_view(), name="update_good"),
    path("goods/<int:pk>", ProductDetailView.as_view(), name="good_detail"),
    path("accounts/profile/", ProfileView.as_view(), name="profile_page"),
]
