from yolov5 import train  # Assuming YOLOv5 is installed locally

if __name__ == "__main__":
    train.run(
        data="data/dataset.yaml",  # Path to dataset configuration
        imgsz=640,
        batch_size=16,
        epochs=50,
        weights="yolov5s.pt",
        project="models",
        name="detection_model",
        exist_ok=True
    )
