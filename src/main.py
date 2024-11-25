import cv2
import os
from detection import detect_labels, recognize_text  # Asegúrate de tener estas funciones
from preprocess import preprocess_image

def process_image(image_path):
    """
    Procesa una sola imagen, detectando etiquetas y reconociendo texto.
    """
    image = cv2.imread(image_path)
    if image is None:
        print(f"No se pudo cargar la imagen: {image_path}")
        return
    
    labels = detect_labels(image)
    recognized_texts = recognize_text(image, labels)

    for i, (text, conf) in enumerate(recognized_texts):
        print(f"Etiqueta {i+1}: {text} (Confianza: {conf:.2f})")
        x1, y1, x2, y2 = labels[i][:4]
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

    # Mostrar la imagen con los resultados
    cv2.imshow(f'Detecciones en {os.path.basename(image_path)}', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Directorio donde están las imágenes
    image_dir = 'data/images'
    
    # Lista todas las imágenes en el directorio
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    # Procesar cada imagen
    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        print(f"Procesando {image_file}...")
        process_image(image_path)

if __name__ == "__main__":
    main()
