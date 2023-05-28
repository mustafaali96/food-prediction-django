from django.urls import path

from revoke_app.views.dish import views

urlpatterns = [
    path("", views.DishAPIView.as_view()),
]