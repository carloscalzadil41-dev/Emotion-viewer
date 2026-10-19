# Lector de Emociones con Inteligencia Artificial

Este es un proyecto en Python que utiliza la cámara web para detectar rostros y analizar emociones en tiempo real utilizando las librerías OpenCV y DeepFace.

## Características
* Detección de emociones en tiempo real.
* Interfaz con caritas ASCII y traducción al español.
* Temporizador que mide la duración de cada emoción.

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Abre la terminal en la carpeta del proyecto y ejecuta el siguiente comando para instalar las dependencias necesarias:

pip install -r requirements.txt

## Uso

Ejecuta el script principal desde tu terminal:

python app.py

*(Nota: La primera vez que se ejecute, DeepFace descargará los pesos del modelo de IA, lo cual puede tardar unos minutos dependiendo de tu conexión a internet).*

Para salir de la cámara, simplemente presiona la tecla `q` en tu teclado.
