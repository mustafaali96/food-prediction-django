from django.urls import path

from revoke_app.views.ingredient import views

urlpatterns = [
    path("", views.IngredientAPIView.as_view()),
]