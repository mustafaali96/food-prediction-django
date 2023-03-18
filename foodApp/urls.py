
from django.urls import path
from .views import RegistrationView, LoginView, LogoutView,ChangePasswordView
from rest_framework_simplejwt import views as jwt_views
from foodApp.views import *

app_name = 'foodApp'

urlpatterns = [
    path('accounts/register', RegistrationView.as_view(), name='register'),
    path('accounts/login', LoginView.as_view(), name='register'),
    path('accounts/logout', LogoutView.as_view(), name='register'),
    path('accounts/change-password', ChangePasswordView.as_view(), name='register'),
    path('accounts/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("getCountry/", GetCountryAPIListView.as_view()),
    path("getCategory/", GetCategoryAPIListView.as_view()),
    path("getDish/", GetDishAPIListView.as_view()),
    path("getIngredient/", GetIngredientAPIListView.as_view())
]