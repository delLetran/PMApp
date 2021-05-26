from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
  login_api,
  auth_api,
  profiles_api, 
  profile_detail_api,
  signup_view,
  profile_list_view,
  profile_view,
  invite_user_api,
)

urlpatterns = [
  path('api/login/', login_api, name="login-api"),
  path('api/auth/', auth_api, name="auth-api"),
  path('api/profile/', profiles_api, name="profiles-api"),
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api/profile/<int:id>/', profile_detail_api, name="profile-detail-api"),
  path('api/invite/<int:id>/', invite_user_api, name="invite-user"),
  path('signup/', signup_view, name="signup"),
  path('profile/', profile_list_view, name="profile-list"),
  path('profile/user/', profile_view, name="profile-detail"),
  # path('profile/<int:id>/', profile_view, name="profile-detail"),
]
