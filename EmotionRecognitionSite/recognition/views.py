from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from torch.distributed.autograd import context

from .forms import ImageFeedForm, VideoFeedForm
from .models import ImageFeed, VideoFeed
from .utils import process_image, process_video


def home(request):
    return render(request, 'recognition/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recognition:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'recognition/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('recognition:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'recognition/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('recognition:login')


@login_required
def dashboard(request):
    image_feeds = ImageFeed.objects.filter(user=request.user)
    video_feeds = VideoFeed.objects.filter(user=request.user)
    context = {
        'image_feeds': image_feeds,
        'video_feeds': video_feeds
    }
    return render(request, 'recognition/dashboard.html', context)


@login_required
def add_image_feed(request):
    if request.method == 'POST':
        form = ImageFeedForm(request.POST, request.FILES)
        if form.is_valid():
            image_feed = form.save(commit=False)
            image_feed.user = request.user
            image_feed.save()
            return redirect('recognition:dashboard')
    else:
        form = ImageFeedForm()
    return render(request, 'recognition/add_image_feed.html', {'form': form})


@login_required
def add_video_feed(request):
    if request.method == 'POST':
        form = VideoFeedForm(request.POST, request.FILES)
        if form.is_valid():
            video_feed = form.save(commit=False)
            video_feed.user = request.user
            video_feed.save()
            return redirect('recognition:dashboard')
    else:
        form = VideoFeedForm()
    return render(request, 'recognition/add_video_feed.html', {'form': form})


@login_required
def process_image_feed(request, feed_id):
    image_feed = get_object_or_404(ImageFeed, id=feed_id, user=request.user)
    process_image(feed_id)
    return redirect('recognition:dashboard')


@login_required
def process_video_feed(request, feed_video_id):
    video_feed = get_object_or_404(VideoFeed, id=feed_video_id, user=request.user)
    process_video(feed_video_id)
    return redirect('recognition:dashboard')


@login_required
def delete_image(request, image_id):
    image = get_object_or_404(ImageFeed, id=image_id, user=request.user)                                     # Ensuring only the owner can delete
    image.delete()
    return redirect('recognition:dashboard')


@login_required
def delete_video(request, video_id):
    video = get_object_or_404(VideoFeed, id=video_id, user=request.user)                                     # Ensuring only the owner can delete
    video.delete()
    return redirect('recognition:dashboard')