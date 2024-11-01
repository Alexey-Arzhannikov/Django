from fer import FER
import cv2
from pprint import pprint
from django.core.files.base import ContentFile
from .models import ImageFeed, DetectedObject

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

        DetectedObject.objects.create(
            image_feed=image_feed,
            object_type=emotion,
            # location=f"{startX},{startY},{endX},{endY}",
            confidence=float(score)
        )

        result, encoded_img = cv2.imencode('.jpg', img)

        # if result:
        #     content = ContentFile(encoded_img.tobytes(), f'processed_{image_feed.image.name}')
        #     image_feed.processed_image.save(content.name, content, save=True)

        return True

    except ImageFeed.DoesNotExist:
        print("ImageFeed not found.")
        return False