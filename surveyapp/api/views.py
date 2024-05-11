from rest_framework import viewsets
from surveyapp.models import survey
from surveyapp.api.serializers import surveySerializer

class SurveyViewSet (viewsets.ModelViewSet):
    queryset = survey.objects.all()
    serializer_class = surveySerializer