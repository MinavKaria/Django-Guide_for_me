from django.shortcuts import render
from django.http import HttpResponse




def  say_hello(request):
    x=11
    y=22
    return HttpResponse('Hello, Djangoo!')

def  say_hello2(request):
    return render(request,'hello.html')

def say_hello3(request):
    return render(request, 'props.html', {'name': 'Minav'})


