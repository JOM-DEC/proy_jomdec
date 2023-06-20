import cv2
import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)
client = boto3.client('rekognition')

def detect_face(collection_id, image_bytes):
    try:
        response = client.search_faces_by_image(
            CollectionId=collection_id,
            Image={'Bytes': image_bytes},
            MaxFaces=1,
            FaceMatchThreshold=80
        )
        if response['FaceMatches']:
            face = response['FaceMatches'][0]['Face']
            external_image_id = face['ExternalImageId']
            confidence = response['FaceMatches'][0]['Face']['Confidence']
            return external_image_id, confidence
        else:
            return None, None
    except ClientError as e:
        logger.exception(f'Failed to detect face: {e}')
        raise

def draw_bounding_box(frame, box, user_id):
    for face in box:
        left = int(face['Left'] * frame.shape[1])
        top = int(face['Top'] * frame.shape[0])
        width = int(face['Width'] * frame.shape[1])
        height = int(face['Height'] * frame.shape[0])

        # Calcular las coordenadas del cuadro de la cara
        right = left + width
        bottom = top + height

        # Dibujar el cuadro delimitador de la cara
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Escribir el user_id
        cv2.putText(frame, f"User ID: {user_id}", (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def detect_and_recognize_faces(collection_id):
    video_capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_roi = frame[y:y + h, x:x + w]
            _, img_encoded = cv2.imencode('.jpg', face_roi)
            image_bytes = img_encoded.tobytes()

            try:
                user_id, confidence = detect_face(collection_id, image_bytes)
                if user_id:
                    draw_bounding_box(frame, [{'Left': x / frame.shape[1], 'Top': y / frame.shape[0],
                                               'Width': w / frame.shape[1], 'Height': h / frame.shape[0]}],
                                      user_id)
                else:
                    # Acciones para manejar un desconocido
                    draw_bounding_box(frame, [{'Left': x / frame.shape[1], 'Top': y / frame.shape[0],
                                               'Width': w / frame.shape[1], 'Height': h / frame.shape[0]}],
                                      "Desconocido")
                    cv2.putText(frame, "Desconocido", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            except Exception as e:
                print(f'Error: {e}')

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

def main():
    collection_id = "safego_empleados"
    detect_and_recognize_faces(collection_id)

if __name__ == "__main__":
    main()