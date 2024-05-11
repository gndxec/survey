from rest_framework import serializers
from surveyapp.models import survey

class surveySerializer(serializers.Serializer):
    class Meta:
        model = survey
        fields = '__all__'
        