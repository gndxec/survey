from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
)
from email_service.api.views import EmailAPIView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include('surveyapp.api.urls')),
    path('send-email', EmailAPIView.as_view(), name='send-email')
]
