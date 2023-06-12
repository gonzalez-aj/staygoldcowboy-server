from django.db import models

class Tag(models.Model):

    medium = models.CharField(max_length=50)
