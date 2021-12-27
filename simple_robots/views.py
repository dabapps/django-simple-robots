from django.conf import settings
from django.views.generic import TemplateView

ROBOTS_ALLOW_HOST_SETTING = "ROBOTS_ALLOW_HOST"
ROBOTS_ALLOW_TEMPLATE = "robots.txt"
ROBOTS_DISALLOW_TEMPLATE = "robots-disallow.txt"


class ServeRobotsView(TemplateView):
    content_type = "text/plain"

    def get_template_names(self):
        robots_allow_host_setting = getattr(settings, ROBOTS_ALLOW_HOST_SETTING, None)
        if (
            robots_allow_host_setting is not None
            and self.request.get_host() in robots_allow_host_setting
        ):
            return ROBOTS_ALLOW_TEMPLATE
        return ROBOTS_DISALLOW_TEMPLATE


serve_robots = ServeRobotsView.as_view()
