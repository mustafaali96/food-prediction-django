from django.urls import path

from revoke_app.views.user_search import views

urlpatterns = [
    path("", views.UserSearchAPIView.as_view()),
]