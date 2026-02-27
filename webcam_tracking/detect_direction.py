import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

hand_landmarker = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

prev_x, prev_y = None, None

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

            # Wrist landmark (0)
            wrist = hand_landmarks[0]

            curr_x = int(wrist.x * width)
            curr_y = int(wrist.y * height)

            cv2.circle(frame, (curr_x, curr_y), 8, (0,255,0), -1)

            if prev_x is not None and prev_y is not None:

                dx = curr_x - prev_x
                dy = curr_y - prev_y

                threshold = 15  

                direction = ""

                if abs(dx) > abs(dy):
                    if dx > threshold:
                        direction = "Right"
                    elif dx < -threshold:
                        direction = "Left"
                else:
                    if dy > threshold:
                        direction = "Down"
                    elif dy < -threshold:
                        direction = "Up"

                if direction:
                    cv2.putText(frame, direction,
                                (50,100),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1, (255,0,0), 3)

            prev_x, prev_y = curr_x, curr_y

    cv2.imshow("Movement Direction", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()