from django.shortcuts import render
from . import machine_learning_model

def home(request):
    return render(request, 'index.html')

def results(request):
    user_name = request.GET['user_name']
    user_name = machine_learning_model.multiplier(user_name)
    return render(request, 'results.html', {'user_name': user_name})