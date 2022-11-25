from django.test import TestCase
from django.test.utils import override_settings


class RobotTestCase(TestCase):
    def test_deny_all(self):
        response = self.client.get("/robots.txt")
        self.assertEqual(response["Content-Type"], "text/plain")
        self.assertEqual(response.content, b"User-agent: *\nDisallow: /\n")

    @override_settings(ROBOTS_ALLOW_HOST="test.com", ALLOWED_HOSTS=["test.com"])
    def test_allow_if_host_matches(self):
        response = self.client.get("/robots.txt", HTTP_HOST="test.com")
        self.assertEqual(response.content, b"User-agent: *\nAllow: /\n")

    @override_settings(ROBOTS_ALLOW_HOST=".test.com", ALLOWED_HOSTS=[".test.com"])
    def test_allow_if_host_matches_wildcard(self):
        response = self.client.get("/robots.txt", HTTP_HOST="example.test.com")
        self.assertEqual(response.content, b"User-agent: *\nAllow: /\n")

    @override_settings(
        ROBOTS_ALLOW_HOSTS=["example.test.com", "example2.test.com"],
        ALLOWED_HOSTS=[".test.com"],
    )
    def test_allow_if_host_matches_multiple(self):
        response = self.client.get("/robots.txt", HTTP_HOST="example2.test.com")
        self.assertEqual(response.content, b"User-agent: *\nAllow: /\n")

    @override_settings(
        ROBOTS_ALLOW_HOST="test.com", ALLOWED_HOSTS=["test.com", "somethingelse.com"]
    )
    def test_deny_if_host_does_not_match(self):
        response = self.client.get("/robots.txt", HTTP_HOST="somethingelse.com")
        self.assertEqual(response.content, b"User-agent: *\nDisallow: /\n")
