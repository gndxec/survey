from rest_framework.routers import DefaultRouter
from surveyapp.api.views import SurveyViewSet

router = DefaultRouter()
router.register('surveys', SurveyViewSet, basename='survey')
urlpatterns = router.urls

