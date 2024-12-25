from django.test import TestCase
import requests
from django.conf import settings

class LangGraphIntegrationTest(TestCase):
    def test_langgraph_api(self):
        # Example code snippet for testing
        test_code = "def add(a, b):\n    return a + b"
        response = requests.post(
            settings.LANGGRAPH_API_URL,
            headers={"Authorization": f"Bearer {settings.LANGGRAPH_API_KEY}"},
            json={"code": test_code, "language": "python"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("suggestions", response.json())
