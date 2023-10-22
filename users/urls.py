from django.urls import path

from .views import (
    UserCreateView,
    UserRetrieveUpdateView,
    CustomObtainAuthTokenView,
    LogoutView,
)


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('me/', UserRetrieveUpdateView.as_view(), name='me'),
    path('token/', CustomObtainAuthTokenView.as_view(), name='token'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
