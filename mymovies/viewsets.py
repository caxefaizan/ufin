from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class CollectionViewSet(viewsets.ModelViewSet):
	queryset = models.Collection.objects.all()
	serializer_class = serializers.CollectionSerializer
	authentication_classes = [JSONWebTokenAuthentication, ]
	permission_classes = [IsAuthenticated, ]
