from django.urls import path
from .views import (
    register_user,
    login_user,
    refresh_token,
    logout_user,
    update_profile,
    get_user_info,
)

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("refresh/", refresh_token, name="refresh"),
    path("logout/", logout_user, name="logout"),
    path("profile/", update_profile, name="update_profile"),
    path("user/<str:username>/", get_user_info, name="get_user_info"),
]
