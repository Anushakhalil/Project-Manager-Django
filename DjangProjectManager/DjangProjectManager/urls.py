from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from user.views import RegisterView, LoginView, LogoutView
from pages.views import homeView, createrPojectView, projectListView, projectDetailsView, sectionView, messengerView, aboutUsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name="index"),
    path('create/', createrPojectView, name="createProjectForm"),
    path('projects/',projectListView, name="projectList" ),
    path('messenger/', messengerView, name="messenger"),
    path('about/', aboutUsView, name="aboutUs"),
    path('login/', LoginView, name="login"),
    path('logout/',LogoutView, name="logout"),
    path('register/', RegisterView, name="register"),
    path('details/', projectDetailsView, name="projectDetails"),
    path('section/', sectionView, name="section"),
    path('', include('pages.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
