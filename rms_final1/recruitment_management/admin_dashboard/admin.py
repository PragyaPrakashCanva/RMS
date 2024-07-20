from django.contrib import admin
from .models import Student, PlacementDrive, Application

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrollment', 'email', 'contact', 'city', 'state')
    search_fields = ('name', 'enrollment', 'email', 'city', 'state')
    list_filter = ('city', 'state', 'gender')
    ordering = ('name',)

@admin.register(PlacementDrive)
class PlacementDriveAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'job_role', 'schedule')
    search_fields = ('company_name', 'job_role')
    list_filter = ('company_name', 'job_role')
    ordering = ('schedule',)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'placement_drive', 'status')
    search_fields = ('student__name', 'placement_drive__company_name', 'status')
    list_filter = ('status',)
    ordering = ('student', 'placement_drive')

# Alternatively, you can use admin.site.register instead of the @admin.register decorator
# admin.site.register(Student, StudentAdmin)
# admin.site.register(PlacementDrive, PlacementDriveAdmin)
# admin.site.register(Application, ApplicationAdmin)
