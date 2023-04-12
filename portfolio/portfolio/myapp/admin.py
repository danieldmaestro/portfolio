from django.contrib import admin
from .models import Dev, Project, Stack, Skill,Visitor

# Register your models here.
admin.site.register(Dev)
admin.site.register(Project)
admin.site.register(Stack)
admin.site.register(Skill)
admin.site.register(Visitor)
