import cv2
from deepface import DeepFace

# Diccionario para traducir las emociones al español
traduccion_emociones = {
    'happy': 'Feliz',
    'sad': 'Triste',
    'angry': 'Enojado',
    'surprise': 'Sorprendido',
    'fear': 'Asustado',
    'disgust': 'Disgustado',
    'neutral': 'Neutral'
}

# Inicializar la cámara
cap = cv2.VideoCapture(0)

print("Iniciando cámara... Presiona la letra 'q' en la ventana para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        resultado = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emocion_ingles = resultado[0]['dominant_emotion'] if isinstance(resultado, list) else resultado['dominant_emotion']
        emocion_espanol = traduccion_emociones.get(emocion_ingles, emocion_ingles)
        cv2.putText(frame, emocion_espanol, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
    except Exception:
        pass

    cv2.imshow('Lector de Emociones AI', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
