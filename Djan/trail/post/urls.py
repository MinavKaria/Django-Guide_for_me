from django.contrib import admin
from django.urls import path, include
from . import views

app_name='post'

urlpatterns = [
    path('post/', views.post_list , name="list"),
    path('post/<slug:slug>/', views.post_page, name="pages"),
    path("new-post/", views.new_post, name="new_post")
]
