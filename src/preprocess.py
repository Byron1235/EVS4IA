import cv2

def preprocess_image(image):
    """
    Preprocesa la imagen para la detección de objetos con YOLOv5.
    """
    # Convertir a RGB (si es necesario) y redimensionar a 640x640
    image_resized = cv2.resize(image, (640, 640))

    # Convertir BGR a RGB si es necesario
    image_rgb = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)

    # Si necesitas hacer más transformaciones (como normalización o eliminación de ruido), puedes hacerlo aquí.
    return image_rgb
