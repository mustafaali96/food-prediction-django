from django.urls import path, include

urlpatterns = [
    path("register/", include("revoke_app.views.register.urls")),
    path("auth/", include("revoke_app.views.login.urls")),
    path("forgot/", include("revoke_app.views.forgot_password.urls")),
    path("food/", include("revoke_app.views.predict.urls")),
    path("contact_us/", include("revoke_app.views.contact_us.urls")),
    path('', include('djoser.urls')),
]