from django.http import HttpResponse
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FeedbackSerializer
from django.shortcuts import render

def home(request):
    return render(request, "reviews/index.html")

def index(request):
    return HttpResponse("Hello, world! Welcome to the Reviews app.")

@api_view(['POST'])
def analyze_code(request):
    # Handle file upload
    file = request.FILES['file']
    code = file.read().decode('utf-8')
    
    # Send to CoAgents
    response = requests.post(
        "https://api.langgraph.cloud/analyze",  # Replace with actual API URL
        headers={"Authorization": "Bearer YOUR_API_KEY"},
        json={"code": code, "language": "python"}
    )
    if response.status_code == 200:
        return Response(response.json())
    else:
        return Response({"error": "Failed to analyze code"}, status=500)

@api_view(['POST'])
def submit_feedback(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Feedback submitted successfully"})
    return Response(serializer.errors, status=400)
