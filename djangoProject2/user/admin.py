from django.contrib import admin

# Register your models here.
from .models import Manager, test
admin.site.register(Manager)
admin.site.register(test)
