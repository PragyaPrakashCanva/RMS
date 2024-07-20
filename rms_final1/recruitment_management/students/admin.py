from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrollment', 'contact', 'email', 'gender', 'city', 'state', '10th', '12th')
    search_fields = ('name', 'enrollment', 'email')
    list_filter = ('gender', 'city', 'state')

admin.site.register(Student, StudentAdmin)
