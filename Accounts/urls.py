from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('token/create/',TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(),name='token_verify'),
    path('signup/',views.SignUpView.as_view(), name='sign_up'),
    path('login/',views.LoginView.as_view(),name='log_in'),
]
