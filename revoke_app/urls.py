from django.urls import path, include

urlpatterns = [
    path("register/", include("revoke_app.views.register.urls")),
    path("auth/", include("revoke_app.views.login.urls")),
    path("forgot/", include("revoke_app.views.forgot_password.urls")),
    path("food/", include("revoke_app.views.predict.urls")),
    path("country/", include("revoke_app.views.country.urls")),
    path("category/", include("revoke_app.views.category.urls")),
    path("foodCategory/", include("revoke_app.views.food_category.urls")),
    path("dishes/", include("revoke_app.views.dish.urls")),
    path("ingredient/", include("revoke_app.views.ingredient.urls")),
    path("contact_us/", include("revoke_app.views.contact_us.urls")),
    path('', include('djoser.urls')),
]