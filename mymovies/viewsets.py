from rest_framework import viewsets
from . import models
from . import serializers

class CollectionViewSet(viewsets.ModelViewSet):
	queryset = models.Collection.objects.all()
	serializer_class = serializers.CollectionSerializer
