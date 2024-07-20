from django.test import TestCase
from .models import Student

class StudentModelTest(TestCase):
    def setUp(self):
        # This method will be run before each test
        self.student = Student.objects.create(
            name='John Doe',
            enrollment='2024001',
            contact='1234567890',
            email='john.doe@example.com',
            gender='Male',
            city='New York',
            state='NY',
            tenth=85,
            twelfth=90
        )

    def test_student_creation(self):
        # Check if the student was created correctly
        self.assertEqual(self.student.name, 'John Doe')
        self.assertEqual(self.student.enrollment, '2024001')
        self.assertEqual(self.student.contact, '1234567890')
        self.assertEqual(self.student.email, 'john.doe@example.com')
        self.assertEqual(self.student.gender, 'Male')
        self.assertEqual(self.student.city, 'New York')
        self.assertEqual(self.student.state, 'NY')
        self.assertEqual(self.student.tenth, 85)
        self.assertEqual(self.student.twelfth, 90)

    def test_student_str(self):
        # Test the __str__ method of the Student model
        self.assertEqual(str(self.student), 'John Doe')
