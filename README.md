# EVS4IA (Environmental Vision System for Artificial Intelligence)

EVS4IA es un sistema de visión por computadora que utiliza redes neuronales y técnicas avanzadas de procesamiento de imágenes para realizar tareas relacionadas con la detección y análisis en imágenes y videos. El proyecto está diseñado para trabajar en un entorno de desarrollo Python utilizando bibliotecas populares como OpenCV, PyTorch y otras herramientas de análisis de imágenes.

## Requisitos

Asegúrate de tener Python 3.7 o superior instalado en tu máquina. Este proyecto utiliza un entorno virtual para gestionar las dependencias.

### Dependencias

- Python 3.7+
- `torch==2.4.1`
- `torchvision==0.17.1`
- `opencv-python==4.5.5.64`
- `pytesseract==0.3.8`
- `PyYAML==6.0`

## Instalación

### 1. Clonar el repositorio

Clona el repositorio a tu máquina local:

git clone https://github.com/tu_usuario/evs4ia.git
cd evs4ia

### 2. Crear un entorno virtual
Crea un entorno virtual para gestionar las dependencias del proyecto:

python -m venv venv

### 3. Activar el entorno virtual
En Windows:
.\venv\Scripts\activate
En Linux/macOS:
source venv/bin/activate

### 4. Instalar las dependencias
Instala las dependencias del proyecto:

pip install -r requirements.txt
Si encuentras problemas con numpy o opencv-python, puedes intentar realizar los pasos recomendados en la sección de Solución de problemas más adelante.

Uso
Ejecutar el script principal
Para ejecutar el sistema de visión en el proyecto, corre el siguiente comando:

python src/main.py
Este comando iniciará el sistema de procesamiento de imágenes utilizando los módulos y configuraciones disponibles.

### Configuración
El archivo config.yaml contiene las configuraciones necesarias para personalizar el comportamiento del sistema. Asegúrate de modificar este archivo según tus necesidades antes de ejecutar el script.

## Solución de problemas
Problema: ModuleNotFoundError: No module named 'cv2'
Si recibes este error, probablemente OpenCV no está instalado correctamente. Puedes intentar reinstalarlo con el siguiente comando:

pip install opencv-python
Problema: ImportError: numpy.core.multiarray failed to import
Este error puede ocurrir debido a una incompatibilidad entre las versiones de numpy y opencv-python. Para solucionarlo, asegúrate de tener las versiones correctas de ambos paquetes:

pip install --upgrade numpy
pip install --upgrade opencv-python
Si el problema persiste, puedes probar la instalación de una versión específica de numpy:

pip install numpy==1.23.5
Problema: RuntimeError: module compiled against ABI version 0x1000009 but this version of numpy is 0x2000000
Este error se debe a una incompatibilidad entre las versiones de numpy y los módulos de OpenCV. Puedes intentar sincronizar las versiones de ambos módulos como se mencionó anteriormente.
