from rest_framework import serializers
from .models import UploadedCode, Feedback

class UploadedCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedCode
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
