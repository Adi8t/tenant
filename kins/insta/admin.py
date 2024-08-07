
# Register your models here.s
from django.contrib import admin
from .models import Client, Domain , UserProfile

admin.site.register(Client)
admin.site.register(Domain)
admin.site.register(UserProfile)