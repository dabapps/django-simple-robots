from django.conf import settings
from django.http.request import validate_host
from django.views.generic import TemplateView

ROBOTS_ALLOW_TEMPLATE = "robots.txt"
ROBOTS_DISALLOW_TEMPLATE = "robots-disallow.txt"


class ServeRobotsView(TemplateView):
    content_type = "text/plain"

    def get_allowed_hosts(self):
        # Maintain singular setting for backwards compatibility
        if getattr(settings, "ROBOTS_ALLOW_HOST", ""):
            return [settings.ROBOTS_ALLOW_HOST]

        return getattr(settings, "ROBOTS_ALLOW_HOSTS", [])

    def get_template_names(self):
        if validate_host(self.request.get_host(), self.get_allowed_hosts()):
            return ROBOTS_ALLOW_TEMPLATE
        return ROBOTS_DISALLOW_TEMPLATE


serve_robots = ServeRobotsView.as_view()
