from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Manager(models.Model):
    username= models.CharField(max_length= 30)
    mongoDbUrl = models.CharField(max_length= 30)
    githubName = models.CharField(max_length= 30)
    githubPassword= models.CharField(max_length= 20)
    picture= models.ImageField(blank=True, null=True, upload_to= 'images/')
    user= models.OneToOneField(User, blank=True, null=True, on_delete= models.CASCADE)
