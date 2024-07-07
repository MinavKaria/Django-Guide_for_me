from django.urls import path
from . import views

# Url configs 
urlpatterns = [
    path('hello/', views.say_hello),
    path('hello-html/', views.say_hello2),
    path('props/', views.say_hello3),
]

