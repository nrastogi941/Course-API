from django.contrib import admin
from .models import CourseModel

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(CourseModel, AuthorAdmin)