"""View module for handling requests about Arts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from staygoldcowboyapi.models import Art, Fan, Tag


class ArtView(ViewSet):
    """SGC Art view"""

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized art instance
        """
        data = request.data
        fan = Fan.objects.get(uid=data["uid"])
        tag_ids = data.pop("tag", [])

        new_art = Art.objects.create(
            fan=fan,
            title=data["title"],
            creation_date=data["creationDate"],
            image_url=data["imageUrl"],
        )

        for tag_id in tag_ids:
            tag = Tag.objects.get(pk=tag_id)
            new_art.tag.add(tag)

        serializer = ArtSerializer(new_art)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        """Handle GET requests for single art

        Returns:
            Response -- JSON serialized art
        """
        try:
            art = Art.objects.get(pk=pk)
            serializer = ArtSerializer(art)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Art.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get All Arts
        and filter Arts by tag
        Returns:
            Response -- JSON serialized list of arts
        """
        arts = Art.objects.all()

        tag = request.query_params.get('tag', None)
        print('tag', tag)
        if tag is not None:
            arts = arts.filter(tag=tag)

        serializer = ArtSerializer(arts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        """Handle PUT requests for an art resource - replaces entire obj

        Returns:
            Response -- Empty body with 204 status code
        """
        data = request.data
        art = Art.objects.get(pk=pk)

        art.title = data["title"]
        art.creation_date = data["creationDate"]
        art.image_url = data["imageUrl"]

        tags = []
        for tag_id in data["tag"]:
            tag = Tag.objects.get(pk=tag_id)
            tags.append(tag)

        art.tag.set(tags)
        art.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ArtFanSerializer(serializers.ModelSerializer):
    """JSON serializer for Fan
    """
    class Meta:
        model = Fan
        fields = ('id', 'uid', 'full_name')

class ArtSerializer(serializers.ModelSerializer):
    """JSON serializer for Art
    """
    fan = ArtFanSerializer(many=False)
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
        depth = 1
