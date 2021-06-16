from django.contrib import admin

# Register your models here.

from .models import Comment, Subject

admin.site.register(Subject)
admin.site.register(Comment)
