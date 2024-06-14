from django.urls import path
from users.views import logout_view, signin_view, signup_view, success_view
from . import views

urlpatterns = [
    path("", views.signin_view, name="sign-in"),
    path("sign-up", views.signup_view, name="sign-up"),
    path("success", views.success_view, name="success"),
    path("log-out", views.logout_view, name="log-out"),
]
