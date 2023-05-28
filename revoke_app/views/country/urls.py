from django.urls import path

from revoke_app.views.country import views

urlpatterns = [
    path("", views.CountryAPIView.as_view()),
]