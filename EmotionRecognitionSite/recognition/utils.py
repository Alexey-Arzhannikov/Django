import os

from fer import FER
from fer import Video
import cv2

from django.core.files.base import ContentFile
from .models import ImageFeed, RecognizedEmotion, VideoFeed


def process_image(image_feed_id):
    """
    Функция распознает эмоции на фото. Выделяет наиболее выраженную.
    Затем передает emotion(распознанная эмоция) и score(значение эмоции от 0 до 1)
    в модель RecognizedEmotion
    """
    try:
        image_feed = ImageFeed.objects.get(id=image_feed_id)
        image_path = image_feed.image.path

        img = cv2.imread(image_path)
        if img is None:
            print("Failed to load image")
            return False

        detector = FER()
        detector.detect_emotions(img)
        emotion, score = detector.top_emotion(img)

        RecognizedEmotion.objects.create(
            info_feed=image_feed,
            emotion=emotion,
            confidence=score
        )
        return True
    except ImageFeed.DoesNotExist:
        print("ImageFeed not found.")
        return False


def process_video(info_feed_video_id):
    """
    Функция распознает эмоции на видео с помощью нейронной сети MTCNN.
    Создает файл .mp4(обработанное видео) и передает в модель VideoFeed
    На основе полученных данных, строит график, также передает в модель VideoFeed
    """
    try:
        info_feed_video = VideoFeed.objects.get(id=info_feed_video_id)
        video_path = info_feed_video.video.path

        video = Video(video_path)
        detector = FER(mtcnn=True)
        raw_data = video.analyze(detector, display=False)

        a = os.getcwd()
        video_name = f'{a}/recognition/media/{info_feed_video.video.name}'
        with open(video_name, 'rb') as f:
            video_content = f.read()
            info_feed_video.processed_video.save(f'processed_video/{info_feed_video.id}.mp4', ContentFile(video_content))

        video.to_pandas(raw_data)
        graph_path = f'recognition/media/graph/processed.png'

        png = cv2.imread(graph_path)
        result, encoded_img = cv2.imencode('.png', png)
        if result:
            content = ContentFile(encoded_img.tobytes(), f'graph_{info_feed_video.id}.png')
            info_feed_video.graph_emotion.save(content.name, content, save=True)

        return True

    except VideoFeed.DoesNotExist:
        print("ImageFeed not found.")
        return False
