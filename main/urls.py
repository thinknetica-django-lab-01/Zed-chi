from django.urls import path, include
from django.contrib.flatpages import views
from .views import homepage


urlpatterns = [
    path("", homepage),
    path('about/', views.flatpage, {'url': '/about/'}, name='about'),
    path('contacts/', views.flatpage, {'url': '/contacts/'}, name='contacts'),
]
