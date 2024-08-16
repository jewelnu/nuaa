# For adding new field like mobile

from django.dispatch import receiver
from django.db.models.signals import post_save
#from .models import Profile

from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import LoginForm,UserCreationForm,Createuserform

from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):

    return render(request, 'login/index.html')


def register(request):
    form = Createuserform(request.POST or None)
    submitted = False
    if request.method == 'POST':
        submitted = True
        if form.is_valid():
            form.save()
            return redirect('my-log')   
    return render(request, 'login/register.html', {'registerform': form,'submitted': submitted})

def my_login(request):

    form = LoginForm()
    if request.method == "POST":
        form= LoginForm(request, data = request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            
    context ={'loginform': form}

    return render(request, 'login/my-login.html',context= context)


def User_logout(request):
    logout(request)
    return redirect('')