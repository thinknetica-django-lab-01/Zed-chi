from django.views.generic import ListView
from django.shortcuts import render
from .models import Product


def homepage(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "guest"
    return render(request, "main/index.html", {"turn_on_block":True, "name":username})

class GoodsListView(ListView):
    model = Product    
    context_object_name = 'goods'
    queryset = Product.objects.all()
    template_name = 'main/goods.html'