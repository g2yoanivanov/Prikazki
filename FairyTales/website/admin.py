from django.contrib import admin

# Register your models here.

from .models import Author, FairyTale

admin.site.register(Author)
admin.site.register(FairyTale)
