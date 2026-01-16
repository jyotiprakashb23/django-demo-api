from django.urls import path
from .views import LoginView, RegisterUserView, UpdateUserView,test_view, ListUsersView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('', test_view, name='test'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path("login/", TokenObtainPairView.as_view(), name="login/get_token"),
    path("login/refresh/", TokenRefreshView.as_view(), name="login/refresh_token"),
    path('users/', ListUsersView.as_view(), name='list_users'),
    path('user-login/', LoginView.as_view(), name='custom_login'),
    path('update-user/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
]
