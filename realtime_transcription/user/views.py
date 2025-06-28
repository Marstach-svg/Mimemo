from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from transcript.models import Meetings
from .forms import CustomSignupForm, LoginForm


def signup_view(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("meeting")
        # フォームが無効な場合はそのまま form を返す（エラー付き）
        else:
            print(form.errors)  # エラーの中身を確認用にログ出力
    else:
        form = CustomSignupForm()

    return render(request, "signup.html", {"form": form})


def login_view(request):

    form = LoginForm()  # ここで事前にformを定義（GETリクエスト時のフォーム）

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("meeting")  # ログイン成功後、メイン画面にリダイレクト
            else:
                form.add_error(None, "無効なメールアドレスまたはパスワードです。")
        else:
            form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")  # ログインページにリダイレクト


@login_required
def mypage_view(request):
    meetings = Meetings.objects.filter(user=request.user).order_by('created_at')
    return render(request, 'mypage.html', {'meetings': meetings})