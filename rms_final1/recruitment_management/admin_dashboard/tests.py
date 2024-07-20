from django.test import TestCase
from django.utils import timezone
from .models import Student, PlacementDrive, Application

class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name='John Doe',
            enrollment='123456',
            email='john.doe@example.com',
            contact='1234567890',
            city='Cityville',
            state='Stateland',
            gender='M'
        )

    def test_student_creation(self):
        """Test the creation of a Student object"""
        student = Student.objects.get(enrollment='123456')
        self.assertEqual(student.name, 'John Doe')
        self.assertEqual(student.email, 'john.doe@example.com')

class PlacementDriveModelTest(TestCase):
    def setUp(self):
        self.placement_drive = PlacementDrive.objects.create(
            company_name='Tech Corp',
            job_role='Software Engineer',
            schedule=timezone.now()
        )

    def test_placement_drive_creation(self):
        """Test the creation of a PlacementDrive object"""
        placement_drive = PlacementDrive.objects.get(company_name='Tech Corp')
        self.assertEqual(placement_drive.job_role, 'Software Engineer')

class ApplicationModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name='John Doe',
            enrollment='123456',
            email='john.doe@example.com',
            contact='1234567890',
            city='Cityville',
            state='Stateland',
            gender='M'
        )
        self.placement_drive = PlacementDrive.objects.create(
            company_name='Tech Corp',
            job_role='Software Engineer',
            schedule=timezone.now()
        )
        self.application = Application.objects.create(
    
