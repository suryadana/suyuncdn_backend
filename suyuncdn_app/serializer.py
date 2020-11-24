from suyuncdn_app.models import Country
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CountryUpdateSerialiser(serializers.Serializer):
    countries = serializers.ListField()
