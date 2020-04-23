from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display= ('title', 'description', )
    list_filter = ('title',)

admin.site.site_header = 'Portfolio Project Admin'
admin.site.register(Project, ProjectAdmin)
