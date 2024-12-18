from django.urls import path

from .views import home, register, user_login, user_logout, dashboard, add_image_feed, add_video_feed, \
    process_image_feed, process_video_feed, delete_image, delete_video

from django.conf import settings
from django.conf.urls.static import static

app_name = 'recognition'

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('process/<int:feed_id>/', process_image_feed, name='process_feed'),
    path('process_video/<int:feed_video_id>/', process_video_feed, name='process_video_feed'),
    path('add-image-feed/', add_image_feed, name='add_image_feed'),
    path('add-video-feed/', add_video_feed, name='add_video_feed'),
    path('image/delete/<int:image_id>/', delete_image, name='delete_image'),
    path('video/delete/<int:video_id>/', delete_video, name='delete_video'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)