from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh_view'),
    path('account/', include('Account.urls')),
    path('contest/', include('Contest.urls')),
]
