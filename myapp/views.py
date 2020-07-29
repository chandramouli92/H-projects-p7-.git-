from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>welcome my world</h1>")
def home(request):
    return render(request,"myapp/base.html")
def child(request):
    return render(request,"child.html")
def cm(request):
    return render(request,"myapp/cm.html")

def sm(request):
    return render(request,"myapp/sample.html")
