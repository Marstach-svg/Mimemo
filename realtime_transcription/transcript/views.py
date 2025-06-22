from django.shortcuts import render, redirect, get_object_or_404
from .models import Meetings
from .forms import MeetingForm


#meeting, transcript, (delete, update関係も追加で作成)
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

def transcript_view(request, meeting_id):
    # meeting_name = Meetings.get()#直前のページで入力した会議名を取ってきたい（redirectで引数として取ってくるかIDとかでmodelから検索かな
    meeting = get_object_or_404(Meetings, id=meeting_id)
    return render(request, "transcript.html", {"meeting": meeting})