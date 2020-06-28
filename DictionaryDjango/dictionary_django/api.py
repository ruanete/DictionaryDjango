from . import models
from . import serializers
from rest_framework import viewsets, permissions


class termViewSet(viewsets.ModelViewSet):
    """ViewSet for the term class"""

    queryset = models.term.objects.all()
    serializer_class = serializers.termSerializer
    permission_classes = [permissions.IsAuthenticated]


class definitionViewSet(viewsets.ModelViewSet):
    """ViewSet for the definition class"""

    queryset = models.definition.objects.all()
    serializer_class = serializers.definitionSerializer
    permission_classes = [permissions.IsAuthenticated]


