from django.db import models

# Create your models here.


class Plan(models.Model):
    name = models.CharField(max_length=100)
    sciName = models.CharField(max_length=100)
    image_url = models.TextField()

    def __str__(self):
        return self.name
