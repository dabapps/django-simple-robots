from django.conf import settings
from django.http import HttpResponse


DENY_ALL = """
User-agent: *
Disallow: /
""".strip()


ALLOW_ALL = """
User-agent: *
Allow: /
""".strip()


ROBOTS_ALLOW_HOST_SETTING = 'ROBOTS_ALLOW_HOST'


def serve_robots(request):
    if getattr(settings, ROBOTS_ALLOW_HOST_SETTING, None) == request.get_host():
        return HttpResponse(ALLOW_ALL, content_type='text/plain')
    return HttpResponse(DENY_ALL, content_type='text/plain')
