django-simple-robots
====================

[![Build Status](https://travis-ci.org/dabapps/django-simple-robots.svg)](https://travis-ci.org/dabapps/django-simple-robots)
[![pypi release](https://img.shields.io/pypi/v/django-simple-robots.svg)](https://pypi.python.org/pypi/django-simple-robots)

Most web applications shouldn't be indexed by Google. This app just provides a view that serves a "deny all" robots.txt.

In some cases, you do want your app to be indexed - but only in your production environment (not any staging environments). For this case, you can set `ROBOTS_ALLOW_HOST`. If the incoming hostname matches this setting, an "allow all" robots.txt will be served. Otherwise, the "deny all" will be served.

Tested against Django 1.8, 1.9, 1.10, 1.11 on Python 2.7, 3.4 and 3.6

### Installation

Install from PIP

    pip install django-simple-robots

In your root urlconf, add an entry as follows:

    from django.conf.urls import url
    from simple_robots.views import serve_robots

    urlpatterns = [
        url(r'robots.txt', serve_robots),
        # ..... other stuff
    ]

Then, add `simple_robots` to `INSTALLED_APPS` in your `settings.py`

Optionally, set `ROBOTS_ALLOW_HOST` settings variable.

    ROBOTS_ALLOW_HOST = "myproductionurl.com"

That's it!

### Customization

The allow and disallow template are stored at `robots.txt` and `robots-disallow.txt` respectively. You can override these in your projects templates directory to customize the responses.

### Code of conduct

For guidelines regarding the code of conduct when contributing to this repository please review [https://www.dabapps.com/open-source/code-of-conduct/](https://www.dabapps.com/open-source/code-of-conduct/)
