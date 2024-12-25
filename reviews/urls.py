from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('analyze-code/', views.analyze_code, name='analyze_code'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
]
