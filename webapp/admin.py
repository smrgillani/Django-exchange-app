from django.contrib import admin
from .Entities.Users import Users
from .Entities.Conversions import Conversions

# Register your models here.
admin.site.register(Users)
admin.site.register(Conversions)