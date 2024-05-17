from django.contrib import admin
from models import AbstractUser, CustomUser

# Register your models here.
admin.site.register(CustomUser, AbstractUser)
