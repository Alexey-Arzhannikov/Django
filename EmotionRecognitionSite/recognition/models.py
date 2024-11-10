from django.db import models
from django.conf import settings


class ImageFeed(models.Model):
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.image.name}"


class RecognizedEmotion(models.Model):
    confidence = models.FloatField(null=True)
    emotion = models.CharField(max_length=30, null=True)
    info_feed = models.ForeignKey(ImageFeed, related_name='recognized_emotions', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.emotion} ({self.confidence}) on {self.info_feed.image.name}"


class VideoFeed(models.Model):
    video = models.FileField(upload_to='videos/')
    processed_video = models.FileField(upload_to='videos/', null=True, blank=True)
    graph_emotion = models.ImageField(upload_to='graph/', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.video.name} - {self.processed_video}"
