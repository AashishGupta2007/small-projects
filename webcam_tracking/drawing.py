import cv2
import mediapipe as mp
import math
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

hand_landmarker = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

canvas = None
prev_x, prev_y = None, None

pinch_threshold = 60

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    height, width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    result = hand_landmarker.detect(mp_image)

    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:

            # ---- Get fingertip positions ----
            thumb = hand_landmarks[4]
            index = hand_landmarks[8]

            x_t = int(thumb.x * width)
            y_t = int(thumb.y * height)

            x_i = int(index.x * width)
            y_i = int(index.y * height)

            # ---- Pinch detection ----
            dist_thumb_index = math.hypot(x_i - x_t, y_i - y_t)

            # ---- Finger state detection (for fist) ----
            index_up  = hand_landmarks[8].y  < hand_landmarks[6].y
            middle_up = hand_landmarks[12].y < hand_landmarks[10].y
            ring_up   = hand_landmarks[16].y < hand_landmarks[14].y
            pinky_up  = hand_landmarks[20].y < hand_landmarks[18].y

            is_fist = (not index_up and
                       not middle_up and
                       not ring_up and
                       not pinky_up)

            # ---- Calculate center of hand (average of 21 points) ----
            avg_x = int(sum(lm.x for lm in hand_landmarks) / 21 * width)
            avg_y = int(sum(lm.y for lm in hand_landmarks) / 21 * height)

            # ---- ERASER (Closed Fist) ----
            if is_fist:
                cv2.putText(frame, "ERASER",
                            (50,100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0,0,255), 3)

                cv2.circle(canvas, (avg_x, avg_y), 40, (0,0,0), -1)
                prev_x, prev_y = None, None

            # ---- DRAW (Pinch) ----
            elif dist_thumb_index < pinch_threshold:
                cv2.putText(frame, "DRAW",
                            (50,100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0,255,0), 3)

                if prev_x is not None:
                    cv2.line(canvas,
                             (prev_x, prev_y),
                             (x_i, y_i),
                             (0, 0, 120), 6)  # Darkest red

                prev_x, prev_y = x_i, y_i

            else:
                prev_x, prev_y = None, None

    combined = cv2.add(frame, canvas)

    cv2.imshow("Air Draw", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()