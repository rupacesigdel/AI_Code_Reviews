from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import FeedbackSerializer
from copilotkit import CopilotKitSDK
import logging
logger = logging.getLogger(__name__)
from .agents import LangGraphAgent

def home(request):
    return render(request, "reviews/index.html")

def index(request):
    return HttpResponse("Hello, world! Welcome to the Reviews app.")



sdk = CopilotKitSDK()

@api_view(['POST'])
def analyze_code(request):
    user_code = request.data.get("code")
    if not user_code:
        return JsonResponse({"error": "No code provided"}, status=400)

    try:
        example_graph = {
            "nodes": [
                {"id": "start", "type": "input"},
                {"id": "summarize", "type": "process", "action": "summarize"},
            ],
            "edges": [
                {"from": "start", "to": "summarize"},
            ],
        }

        lang_agent = LangGraphAgent(name="Summarizer", description="Summarizes user input.", graph=example_graph)

        result = lang_agent.execute(user_code)
        
        return JsonResponse({"result": result})
    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}")
        return JsonResponse({"error": "An error occurred while analyzing the code."}, status=500)


@api_view(['POST'])
def submit_feedback(request):
    """
    Submit user feedback and save it using the serializer.
    """
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Feedback submitted successfully"}, status=201)
    return Response(serializer.errors, status=400)
