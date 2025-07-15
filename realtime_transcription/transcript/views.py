from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Meetings, Minutes
from .forms import MeetingForm
import json
import requests
import os
from django.conf import settings


#meeting, transcript, (delete, update関係も追加で作成)
@login_required
def meeting_view(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():  # フォームのバリデーションが成功した場合
            meeting = form.save(commit=False)  # データベースに保存
            meeting.user = request.user  # 現在ログインしているユーザーをタスクに関連付け
            meeting.save()
            return redirect("transcript", meeting_id=meeting.id)  # 一覧ページにリダイレクト
        else:
            return render(request, "meeting.html", {"form": form})
    else:
        form = MeetingForm()  # フォームが送信されていない場合、空のフォームを表示
    return render(request, "meeting.html", {"form": form})

@login_required
def meeting_edit_view(request, meeting_id):
    meeting = get_object_or_404(Meetings, id=meeting_id, user=request.user)

    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect("transcript", meeting_id=meeting.id)
    else:
        form = MeetingForm(instance=meeting)

    return render(request, "meeting.html", {"form": form, "edit": True, "meeting_id": meeting.id})

@login_required
def transcript_view(request, meeting_id):
    meeting = get_object_or_404(Meetings, id=meeting_id)
    minutes = Minutes.objects.filter(meeting=meeting).first()  # ← 存在すれば取得、なければ None

    return render(request, "transcript.html", {
        "meeting": meeting,
        "minutes": minutes,
    })

@require_POST
@login_required
def save_minutes_view(request):
    try:
        data = json.loads(request.body)
        meeting_id = data.get("meeting_id")
        text = data.get("data", "")
    except (json.JSONDecodeError, TypeError):
        return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)

    meeting = get_object_or_404(Meetings, id=meeting_id)

    minutes, created = Minutes.objects.update_or_create(
        meeting=meeting,
        defaults={"data": text},
    )

    return JsonResponse({
        "status": "success",
        "created": created,
    })

@require_POST
@login_required
def create_minutes_view(request):
    try:
        data = json.loads(request.body)
        meeting_id = data.get("meeting_id")
        transcript = data.get("transcript", "")
    except (json.JSONDecodeError, TypeError):
        return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)

    if not transcript.strip():
        return JsonResponse({"success": False, "error": "Transcript is empty"}, status=400)

    meeting = get_object_or_404(Meetings, id=meeting_id)
    
    # 環境変数からAPIキーを取得
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return JsonResponse({"success": False, "error": "API key not configured"}, status=500)
    
    # OpenAI APIを呼び出して議事録を作成
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "system",
                        "content": "あなたは会議の議事録を作成するアシスタントです。提供された文字起こしテキストから、要点を整理し、読みやすい議事録を作成してください。"
                    },
                    {
                        "role": "user",
                        "content": f"以下の文字起こしテキストから議事録を作成してください：\n\n{transcript}"
                    }
                ],
                "max_tokens": 2000,
                "temperature": 0.3,
            },
            timeout=30
        )
        response.raise_for_status()
        
        result = response.json()
        minutes = result['choices'][0]['message']['content']
        
        return JsonResponse({
            "success": True,
            "minutes": minutes
        })
        
    except requests.exceptions.RequestException as e:
        return JsonResponse({"success": False, "error": f"API request failed: {str(e)}"}, status=500)
    except KeyError as e:
        return JsonResponse({"success": False, "error": f"Unexpected API response format: {str(e)}"}, status=500)
    except Exception as e:
        return JsonResponse({"success": False, "error": f"Unexpected error: {str(e)}"}, status=500)