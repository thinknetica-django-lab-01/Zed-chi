from django.contrib.flatpages import views
from django.urls import path
from .views import homepage

app_name = "main"
urlpatterns = [
    path('', homepage, name="homepage"),
    path('about/', views.flatpage, {'url': '/about/'}, name='about'),
    path('contacts/', views.flatpage, {'url': '/contacts/'}, name='contacts'),
]