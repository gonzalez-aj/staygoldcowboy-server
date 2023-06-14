from django.db import models


class Fan(models.Model):

    uid = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def full_name(self):
        """Additional address field to capture from the client"""
        return f'{self.first_name} {self.last_name}'
