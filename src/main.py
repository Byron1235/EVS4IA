import cv2
import sys
sys.path.append('EVS4IA/yolov5')
from ultralytics import YOLO

from detection import detect_labels, recognize_text
from preprocess import preprocess_image  # Asegúrate de que preprocess_image no cambie a escala de grises

def main():
    # Cargar la imagen
    image = cv2.imread('data/images/test_image.jpg')

    # Preprocesar la imagen
    preprocessed_image = preprocess_image(image)  # Aplica preprocesamiento aquí

    # Detectar etiquetas
    labels = detect_labels(preprocessed_image)

    # Reconocer texto en las etiquetas detectadas
    recognized_texts = recognize_text(preprocess_image, labels)

    # Mostrar los resultados
    for i, (text, conf) in enumerate(recognized_texts):
        print(f"Etiqueta {i+1}: {text} (Confianza: {conf:.2f})")
        x1, y1, x2, y2 = labels[i][:4]
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

    # Mostrar la imagen con las detecciones
    cv2.imshow('Detecciones', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
