import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(path):
    """Load an image from the given path."""
    return cv2.imread(path)

def display_image(image, title="Image"):
    """Display an image using matplotlib."""
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()
