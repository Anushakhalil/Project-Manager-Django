from django.shortcuts import render, redirect

# Create your views here.
from .forms import createUserForm, createUserForm2
from django.contrib.auth import authenticate, login, logout
from .models import Manager


def RegisterView(request):
    form = createUserForm(request.POST, request.FILES)
    form2= createUserForm2(request.POST)

    if request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "POST":
            if form2.is_valid() and form.is_valid():
                obj=Manager.objects.create(
                    username= form.cleaned_data.get('username'),
                    mongoDbUrl= form.cleaned_data.get('mongoDbUrl'),
                    githubName= form.cleaned_data.get('githubName'),
                    githubPassword= form.cleaned_data.get('githubPassword'),
                    picture= form.cleaned_data.get('picture'),
                    user= form2.save()
                )



                return redirect('login')


    context = {
        "form": form,
        "form2": form2
    }
    return render(request, 'register.html', context)


def LoginView(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username= request.POST.get('username')
            password= request.POST.get('password')
            user= authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')

    context = {}
    return render(request, "login.html", context)

def LogoutView(request):
    logout(request)
    return redirect('login')



