from django.urls import path
from simple_robots.views import serve_robots

urlpatterns = [
    path("robots.txt", serve_robots),
]
