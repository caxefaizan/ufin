from mymovies.viewsets import CollectionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('collection',CollectionViewSet)