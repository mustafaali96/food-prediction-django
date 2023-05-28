# Framework imports
from django.urls import path

# App level imports
from revoke_app.views.login import views

urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view()),
    path('logout/', views.UserLogoutAPIView.as_view()),
]
