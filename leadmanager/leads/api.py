from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# lead viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permissions_classes = [permissions.AllowAny]
