import pytesseract
import cv2

class OCRRecognizer:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Path to tesseract executable

    def recognize_text(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray, lang='eng')
        return text
