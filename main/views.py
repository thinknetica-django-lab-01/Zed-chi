from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, Tag


def homepage(request):
    username = (
        request.user.username if request.user.is_authenticated else "Гость"
    )
    return render(
        request, "main/index.html", {"turn_on_block": True, "name": username}
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
                tags__title__contains=self.request.GET.get("tag")
            )
        return qset


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "main/good_detail.html"
