from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "partial/home.html")


def single(request, id=None):
    return render(request, "partial/single.html")