# RMS
Recruitment Management System

Overview
The Recruitment Management System is a web application designed to facilitate recruitment activities within an educational institution. It features separate dashboards for students and administrators, allowing both parties to manage their respective tasks efficiently. The system is built using Django for the backend, and HTML and CSS for the frontend.

Features
Student Dashboard
Login: Authentication system for students.
Upcoming Placement Drive: View upcoming placement drives.
Show All Placement Drives: List all placement drives.
Apply for Industry: Apply for a specific placement drive.
Student Profile: View and update student profile.
Placement History: View the history of applied and attended placement drives.
Admin Dashboard
Login: Authentication system for administrators.
Student Management:
Add, update, and delete student profiles.
Manage academic records and eligibility status.
Add students with minimum details such as Name, Enrollment, Contact, Email, Gender, City, State, 10th, 12th, Resume, Profile Picture.
Bulk student upload via CSV file.
Campus Management:
Add, update, and delete placement drives.
Manage company details, job roles, and schedules.
Report Generation:
Generate reports on student profiles, application status, and placement history.
Generate reports on placement drives, including company participation and student success rates

Usage
Student Dashboard
Login: Navigate to /students/login/ to login.
Upcoming Placement Drive: Navigate to /students/placement_drives/ to view upcoming drives.
Show All Placement Drives: Navigate to /students/show_all_drives/ to view all drives.
Apply for Industry: Navigate to /students/apply/ to apply for a placement drive.
Student Profile: Navigate to /students/profile/ to view and update the profile.
Placement History: Navigate to /students/history/ to view placement history.
Admin Dashboard
Login: Navigate to /admin_dashboard/login/ to login.
Student Management: Navigate to /admin_dashboard/students/ to manage students.
Campus Management: Navigate to /admin_dashboard/placement_drives/ to manage placement drives.
Report Generation: Navigate to /admin_dashboard/reports/ to generate reports.
Contributing
Fork the repository.
Create your feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Create a new Pull Request
