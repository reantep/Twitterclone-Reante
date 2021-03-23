from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class tweet(models.Model):
    id = models.AutoField(primary_key=True)
    parent_tweet_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=14)
    body = models.CharField(max_length=140)
    image = CloudinaryField('image', blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

