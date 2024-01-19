from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    print("running")
    return  render(request, "main/base.html", {})

def body(response):
    return render(response, "main/body.html", {})
