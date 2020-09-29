from django.contrib import admin

# Register your models here.
from .models import toDoListItem,toDoListModel
admin.site.register(toDoListItem)
admin.site.register(toDoListModel)