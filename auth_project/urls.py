from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the API!",
        "endpoints": {
            "register": "/api/users/register/",
            "login": "/api/token/",
            "refresh_token": "/api/token/refresh/",
            "user_profile": "/api/users/me/"
        }
    })

urlpatterns = [
    path('', api_root),  # This handles the root URL
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]