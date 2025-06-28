from django.db import models
from django.contrib.auth import get_user_model


#meetingテーブルとminutesテーブルを以下に作成

class Meetings(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )  # Userが削除されたら削除（CASCADE）
    meeting_name = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Meetings"

    def __str__(self):
        return self.meeting_name


class Minutes(models.Model):
    id = models.AutoField(primary_key=True)
    meeting = models.OneToOneField(Meetings, on_delete=models.CASCADE) # Meetingが削除されたら削除（CASCADE）
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Minutes"

    def __str__(self):
        return self.meeting.meeting_name