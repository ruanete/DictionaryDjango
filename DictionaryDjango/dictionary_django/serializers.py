from . import models

from rest_framework import serializers


class termSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.term
        fields = (
            'pk', 
            'word', 
        )


class definitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.definition
        fields = (
            'pk', 
            'meaning', 
        )


