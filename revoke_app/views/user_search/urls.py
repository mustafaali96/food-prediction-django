from django.urls import path

from revoke_app.views.user_search import views

urlpatterns = [
    path("", views.UserSearchAPIView.as_view()),
    path('create/', views.create_user_search_data, name='create-data'),
    path('trainModel/', views.create_user_search_model, name='create-model'),
]