from django.shortcuts import render # type: ignore

# Create your views here.
from django.shortcuts import render, redirect # type: ignore 
from django.contrib.auth import login, logout, authenticate # type: ignore
from django.views.decorators.csrf import csrf_exempt # type: ignore

from .forms import CustomAuthenticationForm, CustomUserCreationForm

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})

@csrf_exempt
def login_view(request): 
    if request.method == "POST": 
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid(): 
            user = form.get_user() 
            login(request, user)
            return redirect('home') 
    else: 
        form = CustomAuthenticationForm()
    return render(request, 'user/login.html', {'form': form}) 

def logout_view(request): 
    logout(request) 
    return redirect('home')
