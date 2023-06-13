"""View module for handling requests about Arts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from staygoldcowboyapi.models import Art


class ArtView(ViewSet):
    """SGC Art view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single art

        Returns:
            Response -- JSON serialized art
        """
        art = Art.objects.get(pk=pk)
        serializer = ArtSerializer(art)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        """Handle GET requests to get All Art

        Returns:
            Response -- JSON serialized list of art
        """
        arts = Art.objects.all()
        serializer = ArtSerializer(arts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ArtSerializer(serializers.ModelSerializer):
    """JSON serializer for Art
    """
    class Meta:
        model = Art
        fields = (
            'id', 
            'fan', 
            'title', 
            'creation_date', 
            'image_url', 
            'tag'
            )
