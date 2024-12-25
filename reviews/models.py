from django.db import models

class UploadedCode(models.Model):
    file = models.FileField(upload_to='uploaded_code/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    suggestion = models.TextField()
    accepted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
