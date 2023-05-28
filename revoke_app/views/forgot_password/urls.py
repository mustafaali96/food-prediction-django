from django.urls import path

from revoke_app.views.forgot_password import views

urlpatterns = [
    path("password/", views.ChangePasswordView.as_view()),
]