from django.db import models
from user.models import Manager
# Create your models here.

class toDoListModel(models.Model):
    manager= models.OneToOneField(Manager,null=True,blank=True, on_delete=models.CASCADE)

class toDoListItem(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    items = models.ForeignKey(toDoListModel, null=True, blank=True, on_delete=models.SET_NULL)