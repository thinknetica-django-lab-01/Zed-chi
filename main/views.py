from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from allauth.account.views import SignupView as allauth_signup
from allauth.account.views import LoginView as allauth_login
from allauth.account.views import LogoutView as allauth_logout
from .models import Product, Tag
from .forms import ProfileForm, GoodForm


def homepage(request):
    username = (
        request.user.username if request.user.is_authenticated else "Гость"
    )
    return render(
        request, "main/index.html", {"turn_on_block": True, "name": username},
    )


class ProductsListView(ListView):
    paginate_by = 10

    model = Product
    context_object_name = "products"
    queryset = Product.objects.all()
    template_name = "main/goods.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_tag"] = self.request.GET.get("tag")
        context["tags"] = Tag.objects.all()
        return context

    def get_queryset(self):
        qset = super().get_queryset()
        if self.request.GET.get("tag"):
            qset = Product.objects.filter(
                tags__title__contains=self.request.GET.get("tag"),
            )
        return qset


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "main/good_detail.html"


class ProfileView(LoginRequiredMixin, UpdateView):
    login_url = '/admin/'    
    template_name = "main/profile.html"
    form_class = ProfileForm
    success_url = "/goods"
    model = User

    def get_object(self):
        return User.objects.get(id=self.request.user.id)




class AddGoodView(CreateView):
    template_name = "main/add_good_form.html"
    form_class = GoodForm
    model = Product
    success_url = "/goods"


class GoodUpdateView(UpdateView):
    template_name = "main/update_good_form.html"
    form_class = GoodForm
    model = Product
    success_url = "/goods"

class SignUpView(allauth_signup):
    template_name = "account/sign_up.html"
    redirect_field_name = "next"

class LogInView(allauth_login):
    template_name = "account/log_in.html"
    redirect_field_name = "next"    

class LogOutView(allauth_logout):
    template_name = "account/log_out.html"
    redirect_field_name = "next"    
