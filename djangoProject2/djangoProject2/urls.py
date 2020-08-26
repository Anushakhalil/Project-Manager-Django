"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import homeView, createrPojectView, projectListView, projectDetailsView, sectionView, messengerView, aboutUsView, loginView, registerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name="index"),
    path('create/', createrPojectView, name="createProjectForm"),
    path('projects/',projectListView, name="projectList" ),
    path('messenger/', messengerView, name="messenger"),
    path('about/', aboutUsView, name="aboutUs"),
    path('login/', loginView, name="login"),
    path('register/', registerView, name="register"),
    path('details/', projectDetailsView, name="projectDetails"),
    path('section/', sectionView, name="section"),

]
