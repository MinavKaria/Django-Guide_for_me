from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("About")
    return render(request, 'about.html')