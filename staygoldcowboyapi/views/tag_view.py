"""View module for handling requests about Tags"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from staygoldcowboyapi.models import Tag


class TagView(ViewSet):
    """SGC Tag view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized tag
        """
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        """Handle GET requests to get All Tags

        Returns:
            Response -- JSON serialized list of tags
        """
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for Art
    """
    class Meta:
        model = Tag
        fields = (
            'id', 
            'medium'
            )
