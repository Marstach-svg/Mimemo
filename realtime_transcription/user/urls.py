from django.urls import path
from django.contrib.auth.views import PasswordChangeView
from .views import signup_view, login_view, logout_view, mypage_view, user_edit_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("mypage/", mypage_view, name="mypage"),
    path('edit/', user_edit_view, name='user_edit'),
    path('password/', PasswordChangeView.as_view(
        template_name='change_password.html',
        success_url='/mypage/'
    ), name='password_change'),
]