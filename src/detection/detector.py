import torch

class LabelDetector:
    def __init__(self, model_path="yolov5s.pt", confidence_threshold=0.5):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
        self.model.conf = confidence_threshold

    def detect(self, image):
        results = self.model(image)
        return results.xyxy[0].numpy()  # Bounding boxes and labels
