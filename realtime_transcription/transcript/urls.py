from django.urls import path
from .views import meeting_view, transcript_view

urlpatterns = [
    path('meeting/', meeting_view, name="meeting"),
    path('transcript/<int:meeting_id>/', transcript_view, name="transcript")
]