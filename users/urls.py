# users/urls.py
from django.urls import path
from . import views  # Import views from the current app

# Define URL patterns for login, register, and index
urlpatterns = [
    path('', views.index, name='index'),  # Home page that shows index.html
    path('login/', views.login, name='login'),  # Login page route
    path('register/', views.register, name='register'),  # Register page route
]
