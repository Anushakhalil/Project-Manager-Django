from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from user.models import Manager
from .forms import toDoListItemForm
from .models import toDoListModel, toDoListItem

@ login_required(login_url='login')
def homeView(request):
    form= toDoListItemForm(request.POST)
    obj=Manager.objects.get(user=request.user)
    if form.is_valid():
        m=toDoListModel.objects.get(manager=obj)
        toDoListItem.objects.create(
            text= form.cleaned_data.get('text'),
            items= m
        )
    context = {
        "obj": obj,
        "form": form
    }
    return render(request, 'index.html', context)

@ login_required(login_url='login')
def createrPojectView(request):
    return render(request, 'createProjectForm.html',{})

@ login_required(login_url='login')
def projectListView(request):
    return render(request, 'projectList.html', {})

@ login_required(login_url='login')
def projectDetailsView(request):
    return render(request, 'projectDetails.html', {})

@ login_required(login_url='login')
def sectionView(request):
    return render(request, 'section.html', {})

@ login_required(login_url='login')
def messengerView(request):
    return render(request, 'messenger.html', {})

@ login_required(login_url='login')
def aboutUsView(request):
    return render(request, 'aboutUs.html', {})
