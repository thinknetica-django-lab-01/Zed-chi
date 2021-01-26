from django.shortcuts import render


def homepage(request):    
    username = request.user.username if request.user.is_authenticated else "guest"    
    return render(request, "main/index.html", {"turn_on_block":True, "name":username})
