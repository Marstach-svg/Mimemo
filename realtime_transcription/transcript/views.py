from django.shortcuts import render


#meeting, transcript, (delete, update関係も追加で作成)
def meeting_view(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():  # フォームのバリデーションが成功した場合
            meeting = form.save(commit=False)  # データベースに保存
            meeting.user = request.user  # 現在ログインしているユーザーをタスクに関連付け
            meeting.save()
            return redirect("transcript")  # 一覧ページにリダイレクト
        else:
            return render(request, "meeting.html", {"form": form})
    else:
        form = MeetingForm()  # フォームが送信されていない場合、空のフォームを表示
    return render(request, "meeting.html", {"form": form})

def transcript_view(request):
    meeting_name = Meetings.get()#直前のページで入力した会議名を取ってきたい（redirectで引数として取ってくるかIDとかでmodelから検索かな
    return render(request, "transcript.html", meeting_name=meeting_name)