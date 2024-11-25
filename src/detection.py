import pytesseract
from ultralytics import YOLO

# Configurar pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Cargar modelo YOLOv5
model = YOLO('yolov5s.pt')

def detect_labels(image):
    results = model(image, conf=0.7)  # Predicción usando el modelo
    if len(results) > 0:  # Verificar si hay resultados
        labels = results[0].boxes.xyxy.numpy()  # Coordenadas de detección
        return labels
    else:
        return []
    
def recognize_text(image, labels):
    texts = []
    for (x1, y1, x2, y2, conf, cls) in labels:
        cropped = image[int(y1):int(y2), int(x1):int(x2)]
        text = pytesseract.image_to_string(cropped, config='--psm 6')
        texts.append((text.strip(), conf))
    return texts
