from django.contrib import admin
from .models import Client,Work,Artist
# Register your models here.

admin.site.register(Client)
admin.site.register(Artist)
admin.site.register(Work)