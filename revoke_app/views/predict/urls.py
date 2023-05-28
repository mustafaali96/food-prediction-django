# Framework imports
from django.urls import path

# App level imports
from revoke_app.views.predict import views

urlpatterns = [
    path('predict/', views.PredictFoodAPIView.as_view()),
]
