from django.db import models
from .tag import Tag

class Art(models.Model):
    Fan = models.ForeignKey(
        "Fan", on_delete=models.CASCADE, related_name='art_fan')
    title = models.CharField(max_length=50)
    creation_date = models.DateField()
    image_url = models.URLField()
    tag = models.ManyToManyField(
        Tag, related_name='art_tags')
