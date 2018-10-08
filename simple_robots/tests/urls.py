from django.conf.urls import url
from simple_robots.views import serve_robots


urlpatterns = [
    url(r'robots.txt', serve_robots),
]
