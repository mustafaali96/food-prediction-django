from django.urls import path

from revoke_app.views.food_category import views

urlpatterns = [
    path("", views.FoodCategoryAPIView.as_view()),
]