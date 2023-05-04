from django.shortcuts import render,redirect
from .forms import RegForm, AdminForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


# Create your views here.

def page(request):
    return render(request, 'page.html')

def fomu(request):
    if request.method == 'POST':
        form= RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingia')
    else:
        form= RegForm() 
    return render(request, 'signup.html',{'form' : form})

def adminfomu(request):
    if request.method == 'POST':
        form= AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingia')
    else:
        form= AdminForm() 
    return render(request, 'signup.html',{'form' : form})


def ingia(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        print (username, password)
        print(type(user))
        if user is not None:
            login(request, user)
            return redirect('ad')
        
        else:
            messages.error(request,'INVALID CREDENTIALS')
            return redirect('ingia')   

    else:
        return render(request, 'log.html')


def ad(request):
    return render(request, 'dashboard.html')
