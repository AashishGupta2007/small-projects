import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Load model
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

            # Check finger states (ignore thumb for simplicity)
            index_up  = hand_landmarks[8].y  < hand_landmarks[6].y
            middle_up = hand_landmarks[12].y < hand_landmarks[10].y
            ring_up   = hand_landmarks[16].y < hand_landmarks[14].y
            pinky_up  = hand_landmarks[20].y < hand_landmarks[18].y

            # Convert normalized → pixel for drawing (optional)
            for landmark in hand_landmarks:
                x = int(landmark.x * width)
                y = int(landmark.y * height)
                cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

            # Gesture decision
            if index_up and middle_up and ring_up and pinky_up:
                cv2.putText(frame, "OPEN HAND",
                            (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 3)

            elif not index_up and not middle_up and not ring_up and not pinky_up:
                cv2.putText(frame, "FIST",
                            (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 3)

    cv2.imshow("Open Hand vs Fist", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()