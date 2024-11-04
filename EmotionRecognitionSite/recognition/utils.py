from fer import FER
import cv2
from .models import ImageFeed, RecognizedEmotion

def process_image(image_feed_id):

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

