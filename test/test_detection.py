import cv2
from detection import detect_labels

def test_detect_labels():
    image = cv2.imread('data/images/test_image.jpg')
    labels = detect_labels(image)
    assert len(labels) > 0  # Esperamos al menos una detección
