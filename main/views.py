from django.shortcuts import render


def homepage(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "guest"
    return render(request, "main/index.html", {"turn_on_block":True, "name":username})
