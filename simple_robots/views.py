from django.conf import settings
from django.views.generic import TemplateView


ROBOTS_ALLOW_HOST_SETTING = 'ROBOTS_ALLOW_HOST'
ROBOTS_ALLOW_TEMPLATE = "robots.txt"
ROBOTS_DISALLOW_TEMPLATE = "robots-disallow.txt"


class ServeRobotsView(TemplateView):
    content_type = "text/plain"

    def get_template_names(self):
        if getattr(settings, ROBOTS_ALLOW_HOST_SETTING, None) == self.request.get_host():
            return ROBOTS_ALLOW_TEMPLATE
        return ROBOTS_DISALLOW_TEMPLATE


serve_robots = ServeRobotsView.as_view()
