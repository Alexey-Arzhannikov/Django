from django import forms
from .models import ImageFeed, VideoFeed


class ImageFeedForm(forms.ModelForm):
    class Meta:
        model = ImageFeed
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }
        help_texts = {
            'image': 'Upload an image file.',
        }


class VideoFeedForm(forms.ModelForm):
    class Meta:
        model = VideoFeed
        fields = ['video']
        widgets = {
            'video': forms.FileInput(attrs={'accept': 'video/*'}),
        }
        help_texts = {
            'video': 'Upload an videos file.',
        }
