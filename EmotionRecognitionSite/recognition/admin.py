from django.contrib import admin
from .models import ImageFeed, RecognizedEmotion, VideoFeed

admin.site.register(ImageFeed)
admin.site.register(RecognizedEmotion)
admin.site.register(VideoFeed)
# admin.site.register(VideoEmotion)