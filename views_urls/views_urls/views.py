"""
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World! This is the Home Page.")
"""
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')