from django.conf import settings
from django.views.generic import TemplateView


ROBOTS_ALLOW_HOST_SETTING = 'ROBOTS_ALLOW_HOST'


class ServeRobotsView(TemplateView):
    content_type = "text/plain"

    def get_template_names(self):
        if getattr(settings, ROBOTS_ALLOW_HOST_SETTING, None) == self.request.get_host():
            return "robots.txt"
        return "robots-disallow.txt"
