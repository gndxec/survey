from rest_framework.routers import DefaultRouter
from surveyapp.api.views import surveyViewSet

router = DefaultRouter()
router.register('surveys', surveyViewSet, basename='survey')
urlpatterns = [
    router.urls
]
