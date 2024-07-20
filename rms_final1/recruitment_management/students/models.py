# students/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    tenth_grade = models.DecimalField(max_digits=5, decimal_places=2)
    twelfth_grade = models.DecimalField(max_digits=5, decimal_places=2)
    resume = models.FileField(upload_to='resumes/')
    profile_picture = models.ImageField(upload_to='profile_pictures/')

class PlacementDrive(models.Model):
    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    schedule = models.DateTimeField()
    description = models.TextField()

class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    placement_drive = models.ForeignKey(PlacementDrive, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
