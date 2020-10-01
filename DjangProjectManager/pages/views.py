from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
# Create your views here.
from user.models import Manager
from .forms import toDoListItemForm, projectForm
from .models import toDoListModel, toDoListItem, projectModel
from github import Github


@ login_required(login_url='login')
def homeView(request):
    form= toDoListItemForm(request.POST)
    obj=Manager.objects.get(user=request.user)
    m = toDoListModel.objects.get(manager=obj)
    if form.is_valid():

        t=form.cleaned_data.get('text')
        if t is not None:
            toDoListItem.objects.create(
                text= t,
                items= m
            )
            
    items= m.todolistitem_set.all()
    
    class Git:
        def __init__(self, name, commits, pullReq_o, pullReq_c, issues, sr):
            self.name = name
            self.commits = commits
            self.pullReq_o = pullReq_o
            self.pullReq_c = pullReq_c
            self.issues = issues
            self.sr = sr
    g= Github(obj.githubName,obj.githubPassword)
    lst=[]
    for i,repo in enumerate(g.get_user().get_repos()):
        if i == 3:
            break
        try:
            C=len(list(repo.get_commits()))
        except:
            C=0
        ob=Git(repo.name,C,len(list(repo.get_pulls(state='open'))),len(list(repo.get_pulls(state='closed'))),len(list(repo.get_issues())),i+1)
        lst.append(ob)


    context = {
        "obj": obj,
        "form": form,
        "items":items,
        "lst":lst
    }
    return render(request, 'index.html', context)

@ login_required(login_url='login')
def createrPojectView(request):
    obj=Manager.objects.get(user=request.user)
    g= Github(obj.githubName,obj.githubPassword)
    lst = [obj.githubName]

    form = projectForm(request.POST)
    if form.is_valid():
        repo_name = form.cleaned_data.get('name')
        repo_desc = form.cleaned_data.get('description')
        repo_access = form.cleaned_data.get('access')
        repo_fields = form.cleaned_data.get('fields')
        if repo_name != "" and repo_desc != "" and len(repo_fields) != 0 and repo_access != "":
            pObj = projectModel.objects.create(
                name = repo_name,
                description = repo_desc,
                access = repo_access,
                requrirements_field = "Requirements" in repo_fields,
                wireframes_field = "Wireframes" in repo_fields,
                logo_field = "Logo" in repo_fields,
                designing_field = "Designing" in repo_fields,
                development_field = "Development" in repo_fields,
            )
            g.get_user().create_repo(
                repo_name,
                description=repo_desc,
                private= "private" in repo_access
            )
            
            return redirect('projectDetails', project_id=pObj.id)

    

    context = {
        "lst":obj.githubName,
        "form": form,
        
    }
    return render(request, 'createProjectForm.html',context)

@ login_required(login_url='login')
def projectListView(request):
    return render(request, 'projectList.html', {})

@ login_required(login_url='login')
def projectDetailsView(request, project_id):
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

@login_required(login_url='login')
def deleteTodo(request, todo_id):
    a = toDoListItem.objects.get(id=todo_id)
    a.delete()
    return redirect('index')

