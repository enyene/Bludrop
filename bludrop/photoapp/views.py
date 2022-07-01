from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'photoapp/index.html')

def signup(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username= username,password= password)
            login(request,user)
            return redirect('home')

        else:
            form = UserCreationForm()
            return render(request,'photoapp/signup.html',{'form':form})

    else:
        form = UserCreationForm()
        return render(request,'photoapp/signup.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username= username,password= password)
            login(request,user)
            return redirect('home')
        else:
            form = UserCreationForm()
            return render(request,'photoapp/signup.html',{'form':form})
    else:
         form = UserCreationForm()
         return render(request,'photoapp/signup.html',{'form':form})