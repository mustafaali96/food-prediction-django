from django.urls import path

from revoke_app.views.category import views

urlpatterns = [
    path("", views.CategoryAPIView.as_view()),
]