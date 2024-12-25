from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='index'),
    path('analyze-code/', views.analyze_code, name='analyze_code'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)