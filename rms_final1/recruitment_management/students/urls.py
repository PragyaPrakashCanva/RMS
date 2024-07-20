# students/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='student_login'),
    path('upcoming/', views.upcoming_placement_drives, name='upcoming_placement_drives'),
    path('all/', views.all_placement_drives, name='all_placement_drives'),
    path('apply/<int:drive_id>/', views.apply_for_industry, name='apply_for_industry'),
    path('profile/', views.student_profile, name='student_profile'),
    path('history/', views.placement_history, name='placement_history'),
]

# admin_dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='admin_login'),
    path('student_management/', views.student_management, name='student_management'),
    path('add_student/', views.add_student, name='add_student'),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('campus_management/', views.campus_management, name='campus_management'),
    path('add_drive/', views.add_drive, name='add_drive'),
    path('update_drive/<int:drive_id>/', views.update_drive, name='update_drive'),
    path('delete_drive/<int:drive_id>/', views.delete_drive, name='delete_drive'),
    path('generate_reports/', views.generate_reports, name='generate_reports'),
]
