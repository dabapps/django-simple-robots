from django.conf.urls import url
from simple_robots.views import ServeRobotsView


urlpatterns = [
    url(r'robots.txt', ServeRobotsView.as_view()),
]
