from django.shortcuts import render

# Create your views here.
def homepage(req):
    return render(req, "index.html")