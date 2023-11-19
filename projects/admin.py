from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from projects.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    pass