from rest_framework import serializers
from . models import Collection, Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    # movie = MovieSerializer(read_only=True, many=True)

    class Meta:
        model = Collection
        fields = '__all__'

    # def create(self, validated_data):
    #     movie = validated_data.pop('movie')
    #     movie = Movie .objects.create(**movie )
    #     collection = Collection.objects.create(movie=movie, **validated_data)
    #     return collection
