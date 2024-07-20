from django.apps import AppConfig

class StudentsConfig(AppConfig):
    name = 'students'
    verbose_name = 'Students Management'

    def ready(self):
        # This method is called when the app is loaded
        # You can put app initialization code here if needed
        pass
