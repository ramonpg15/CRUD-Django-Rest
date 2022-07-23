"""escuela URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from escuelav1.api import RegisterApi
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/login/', include("rest_framework.urls")),
    path('escuelav1/', include('escuelav1.urls')),
    # path('auth/login',LoginView.as_view(),name='Login'),
    # urls del rest_framework
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/register', RegisterApi.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
    path('biblioteca/', include('biblioteca.urls'))
]
# requirements,