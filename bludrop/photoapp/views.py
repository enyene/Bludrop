from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from .models import Photo,Comment

# Create your views here.

class PhotoListView(ListView):
    model = Photo
    
class PhotoCreateView(CreateView):
    model = Photo
    fields = ('name','description')


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('photoapp:photo')


class PhotoDetailView(DetailView):
    model = Photo
    #get_context_data = 'photos'
    template_name = 'photoapp/photo_detail.html'

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = [
        'description'
    ]


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


def logout(request):
    logout(request)
    return redirect('home')