from django.contrib import admin

# Register your models here.
from .models import toDoListItem,toDoListModel, projectModel
admin.site.register(toDoListItem)
admin.site.register(toDoListModel)
admin.site.register(projectModel)