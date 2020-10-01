from django.db import models
from django.urls import reverse

from user.models import Manager
# Create your models here.
class toDoListModel(models.Model):
    manager= models.OneToOneField(Manager,null=True,blank=True, on_delete=models.CASCADE)

class toDoListItem(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    items = models.ForeignKey(toDoListModel, null=True, blank=True, on_delete=models.SET_NULL)

    def returnURL(self):
        return reverse('Todo:todo', kwargs={"todo_id": self.id})

class projectModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length= 1000)
    access = models.CharField(max_length=100)
    requrirements_field = models.BooleanField()
    wireframes_field = models.BooleanField()
    logo_field = models.BooleanField()
    designing_field = models.BooleanField()
    development_field = models.BooleanField()
