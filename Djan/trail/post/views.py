from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'posts': post})
    # return HttpResponse(slug)

@login_required(login_url='/users/login/')
def new_post(request):
    if request.method == 'POST':
        print('POST')
        form=forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            print('VALID')
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('post:list')
        else:
            return HttpResponse('Invalid form')
    else:
        print('GET')
        form=forms.PostForm()
        return render(request, 'posts/post_new.html',{'form':form})