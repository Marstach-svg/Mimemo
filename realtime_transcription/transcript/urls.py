from django.urls import path
from .views import meeting_view, meeting_edit_view, transcript_view, save_minutes_view, create_minutes_view

urlpatterns = [
    path('meeting/', meeting_view, name="meeting"),
    path("meeting/<int:meeting_id>/edit/", meeting_edit_view, name="meeting_edit"),
    path('transcript/<int:meeting_id>/', transcript_view, name="transcript"),
    path('save-minutes/', save_minutes_view, name="save_minutes"),
    path('create-minutes/', create_minutes_view, name="create_minutes"),
]