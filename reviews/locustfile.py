from locust import HttpUser, task

class LoadTest(HttpUser):
    @task
    def analyze_code(self):
        code = "def multiply(a, b): return a * b"
        self.client.post(
            "/analyze-code/",
            files={"file": ("test.py", code)}
        )
