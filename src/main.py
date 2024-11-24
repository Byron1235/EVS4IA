import cv2
from detection.detector import LabelDetector
from recognition.ocr import OCRRecognizer
from utils import load_image, display_image

def main(image_path):
    # Load image
    image = load_image(image_path)

    # Detect labels
    detector = LabelDetector(model_path="models/detection_model.pt", confidence_threshold=0.5)
    detections = detector.detect(image)

    # Recognize text
    recognizer = OCRRecognizer()
    for box in detections:
        x1, y1, x2, y2, conf, cls = map(int, box[:6])
        roi = image[y1:y2, x1:x2]  # Crop region of interest
        text = recognizer.recognize_text(roi)
        print(f"Detected text: {text}")

        # Draw bounding box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display results
    display_image(image, title="Detection Results")

if __name__ == "__main__":
    image_path = "data/raw/sample.jpg"
    main(image_path)
