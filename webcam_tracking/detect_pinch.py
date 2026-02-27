import cv2
import mediapipe as mp
import math
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

hand_landmarker = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    result = hand_landmarker.detect(mp_image)

    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:

            # Get thumb tip (4) and index tip (8)
            thumb = hand_landmarks[4]
            index = hand_landmarks[8]

            # Convert normalized → pixel
            x1 = int(thumb.x * width)
            y1 = int(thumb.y * height)

            x2 = int(index.x * width)
            y2 = int(index.y * height)

            # Draw circles
            cv2.circle(frame, (x1, y1), 8, (0, 255, 0), -1)
            cv2.circle(frame, (x2, y2), 8, (0, 255, 0), -1)

            # Draw line between them
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

            # Calculate distance
            distance = math.hypot(x2 - x1, y2 - y1)

            # Pinch threshold (adjust if needed)
            if distance < 60:
                cv2.putText(frame, "PINCH",
                            (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 3)

    cv2.imshow("Pinch Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()