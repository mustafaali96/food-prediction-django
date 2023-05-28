from django.urls import path, include
from rest_framework.routers import DefaultRouter

from revoke_app.views.register import views

router = DefaultRouter()

router.register("", views.UserSignUpCreateView, basename="register_url")

urlpatterns = [
    path("", include(router.urls))
]