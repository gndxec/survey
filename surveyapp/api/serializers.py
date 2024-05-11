from rest_framework import serializers
from surveyapp.models import survey

class surveySerializer(serializers.ModelSerializer):
    class Meta:
        model = survey
        fields = '__all__'
        