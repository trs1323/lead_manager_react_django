from rest_framework import serializers
from .models import Lead

# leads serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

