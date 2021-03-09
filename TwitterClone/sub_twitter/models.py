from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class tweet(models.Models):
    name = models.CharField(max_length=14)
    body = models.CharField(max_length=140)
    image = CloudinaryField('image')
    like_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name
