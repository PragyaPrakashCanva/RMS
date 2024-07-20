# students/views.py
from django.shortcuts import render
from .models import PlacementDrive, Application, Student

def login(request):
    return render(request, 'students/login.html')

def upcoming_placement_drives(request):
    drives = PlacementDrive.objects.filter(schedule__gte=timezone.now())
    return render(request, 'students/upcoming_placement_drives.html', {'drives': drives})

def all_placement_drives(request):
    drives = PlacementDrive.objects.all()
    return render(request, 'students/all_placement_drives.html', {'drives': drives})

def apply_for_industry(request, drive_id):
    drive = PlacementDrive.objects.get(id=drive_id)
    if request.method == 'POST':
        Application.objects.create(student=request.user.student, placement_drive=drive, status='Applied')
    return render(request, 'students/apply_for_industry.html', {'drive': drive})

def student_profile(request):
    student = request.user.student
    return render(request, 'students/student_profile.html', {'student': student})

def placement_history(request):
    applications = Application.objects.filter(student=request.user.student)
    return render(request, 'students/placement_history.html', {'applications': applications})

# admin_dashboard/views.py
from django.shortcuts import render, redirect
from .models import Student, PlacementDrive
import csv

def login(request):
    return render(request, 'admin_dashboard/login.html')

def student_management(request):
    students = Student.objects.all()
    return render(request, 'admin_dashboard/student_management.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        # Code to add student
    return render(request, 'admin_dashboard/add_student.html')

def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        # Code to update student
    return render(request, 'admin_dashboard/update_student.html', {'student': student})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('student_management')

def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        reader = csv.reader(csv_file)
        for row in reader:
            # Code to process each row and create Student
    return render(request, 'admin_dashboard/upload_csv.html')

def campus_management(request):
    drives = PlacementDrive.objects.all()
    return render(request, 'admin_dashboard/campus_management.html', {'drives': drives})

def add_drive(request):
    if request.method == 'POST':
        # Code to add drive
    return render(request, 'admin_dashboard/add_drive.html')

def update_drive(request, drive_id):
    drive = PlacementDrive.objects.get(id=drive_id)
    if request.method == 'POST':
        # Code to update drive
    return render(request, 'admin_dashboard/update_drive.html', {'drive': drive})

def delete_drive(request, drive_id):
    drive = PlacementDrive.objects.get(id=drive_id)
    drive.delete()
    return redirect('campus_management')

def generate_reports(request):
    # Code to generate reports
    return render(request, 'admin_dashboard/generate_reports.html')
