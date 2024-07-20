from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),  # Includes URLs from the 'students' app
    path('admin-dashboard/', include('admin_dashboard.urls')),  # Includes URLs from the 'admin_dashboard' app
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
