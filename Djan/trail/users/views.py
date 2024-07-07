from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    if request.method == "POST": 
        form = UserCreationForm(request.POST) 
        print("Hello")
        if form.is_valid(): 
            login(request, form.save())
            return redirect("post:list")
        
        else:
            print("Not valid")
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, "register.html", { "form": form })

def login_view(request):
    # return render(request, "login.html")
    if request.method == "POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("post:list")
        else:
            print(form.errors)
    else: 
        form=AuthenticationForm()
    return render(request, "login.html", { "form": form })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("post:list")