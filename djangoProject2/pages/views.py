from django.shortcuts import render

# Create your views here.

def homeView(request):
    return render(request, 'index.html', {})

def createrPojectView(request):
    return render(request, 'createProjectForm.html',{})

def projectListView(request):
    return render(request, 'projectList.html', {})

def projectDetailsView(request):
    return render(request, 'projectDetails.html', {})

def sectionView(request):
    return render(request, 'section.html', {})

def messengerView(request):
    return render(request, 'messenger.html', {})

def aboutUsView(request):
    return render(request, 'aboutUs.html', {})

def loginView(request):
    return render(request, 'login.html', {})

def registerView(request):
    return render(request, 'register.html', {})
