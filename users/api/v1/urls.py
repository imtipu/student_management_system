from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from users.api.v1 import views as api_views
urlpatterns = [
    path('login/token/', obtain_jwt_token, name='token_obtain'),
    path('login/token/refresh/', refresh_jwt_token, name='token_refresh'),
    path('login/token/verify/', verify_jwt_token, name='token_verify'),
    path('user/profile/', api_views.LoggedUserProfile.as_view(), name='token_verify'),
]