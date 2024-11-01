from django.db import models
from django.conf import settings

# Create your models here.
class ImageFeed(models.Model):

    image = models.ImageField(upload_to='images/')
    confidence = models.FloatField(null=True)
    emotion = models.CharField(max_length=30, null=True)
    # processed_image = models.ImageField(upload_to='processed_images/', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.image.name}"


class DetectedObject(models.Model):

    object_type = models.CharField(max_length=100)
    confidence = models.FloatField()
    location = models.CharField(max_length=255)
    image_feed = models.ForeignKey(ImageFeed, related_name='recognized_emotions', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.object_type} ({self.confidence * 100}%) on {self.image_feed.image.name}"