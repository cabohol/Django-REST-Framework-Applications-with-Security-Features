# main urls.py (project/urls.py)
from django.contrib import admin
from django.urls import path, include

# URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page
    path('', include('users.urls')),  # Include the 'users' app URLs for all routes in the app
]
