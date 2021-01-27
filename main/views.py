from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Product


def homepage(request):    
    username = request.user.username if request.user.is_authenticated else "Гость"    
    return render(request, "main/index.html", {"turn_on_block":True, "name":username})

class ProductsListView(ListView):
    model = Product    
    context_object_name = 'products'
    queryset = Product.objects.all()
    template_name = 'main/goods.html'

class ProductDetailView(DetailView):
    model = Product    
    context_object_name = 'product'   
    template_name = 'main/good_detail.html'    