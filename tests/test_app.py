import unittest
from pathlib import Path

from index import AFFILIATE_URL, app


class NerveCalmSiteTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_public_routes_render(self):
        for route in ("/", "/privacy", "/terms", "/disclaimer", "/robots.txt"):
            response = self.client.get(route)
            self.assertEqual(response.status_code, 200, route)
            response.close()

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_affiliate_url_is_used_on_homepage(self):
        html = self.client.get("/").get_data(as_text=True)
        self.assertGreaterEqual(html.count(AFFILIATE_URL.replace("&", "&amp;")), 10)
        self.assertIn('rel="sponsored nofollow noopener"', html)

    def test_homepage_contains_disclosures(self):
        html = self.client.get("/").get_data(as_text=True)
        self.assertIn("Affiliate disclosure", html)
        self.assertIn("not intended to diagnose, treat, cure, or prevent", html)

    def test_security_headers(self):
        response = self.client.get("/")
        self.assertEqual(response.headers["X-Content-Type-Options"], "nosniff")
        self.assertEqual(response.headers["X-Frame-Options"], "SAMEORIGIN")

    def test_mobile_product_image_keeps_its_natural_height(self):
        css = Path(app.static_folder, "css", "style.css").read_text(encoding="utf-8")
        self.assertIn(".hero-product-card > img", css)
        self.assertIn("height: auto;", css)
        self.assertIn("width: min(100%, 380px);", css)


if __name__ == "__main__":
    unittest.main()
