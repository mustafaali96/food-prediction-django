from django.urls import path

from revoke_app.views.contact_us import views

urlpatterns = [
    path("", views.ContactUsAPIView.as_view()),
]