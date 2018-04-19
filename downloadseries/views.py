from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def search(request):
    return render(request, 'home/index.html')
