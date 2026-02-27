# Hand Motion Tracking (Python)

A real-time hand tracking and gesture detection project using OpenCV and
MediaPipe.

This project captures webcam input, detects hand landmarks, and performs
gesture-based analysis such as fist detection, pinch detection,
direction detection, and coordinate tracking.

------------------------------------------------------------------------

## Features

-   Real-time webcam hand tracking
-   21-point hand landmark detection
-   Fist detection
-   Pinch detection
-   Hand direction detection
-   Coordinate tracking
-   Basic drawing utilities
-   Modular script structure

------------------------------------------------------------------------

## Technologies Used

-   Python
-   OpenCV
-   MediaPipe
-   NumPy

------------------------------------------------------------------------

## Project Structure

webcam_tracking/ │ ├── test_camera.py \# Tests webcam feed ├──
21_points.py \# Displays 21 MediaPipe hand landmarks ├──
hand_landmarker_task \# MediaPipe task/model file ├── detect_fist.py \#
Detects closed fist gesture ├── detect_pinch.py \# Detects pinch gesture
├── detect_direction.py \# Detects hand movement direction ├──
coordinate_track.py \# Tracks hand coordinates ├── drawing.py \# Drawing
utilities on frame ├── requirements.txt \# Project dependencies └──
README.md

------------------------------------------------------------------------

## Installation

1.  Create virtual environment:

    python -m venv venv

2.  Activate it:

    macOS/Linux: source venv/bin/activate

    Windows: venv`\Scripts`{=tex}`\activate`{=tex}

3.  Install dependencies:

    pip install -r requirements.txt

------------------------------------------------------------------------

## Usage

Run any module individually:

python test_camera.py python 21_points.py python detect_fist.py python
detect_pinch.py python detect_direction.py python coordinate_track.py

Each script demonstrates a specific functionality.

------------------------------------------------------------------------

## How It Works

-   MediaPipe detects 21 hand landmarks from webcam frames.
-   OpenCV captures and displays the video stream.
-   Landmark coordinates are processed to determine gestures.
-   Custom logic interprets distances and relative positions of fingers.

------------------------------------------------------------------------

## Learning Objectives

This project demonstrates:

-   Real-time computer vision processing
-   Landmark-based gesture recognition
-   Frame-by-frame video analysis
-   Modular Python project structure
-   Working with MediaPipe Tasks API

------------------------------------------------------------------------

## Limitations

-   Single-hand tracking focus
-   No GUI beyond OpenCV window
-   No model training (uses pretrained MediaPipe model)

------------------------------------------------------------------------

## Future Improvements

-   Multi-hand tracking
-   Gesture-to-action mapping
-   GUI-based interface
-   Integration with 3D graphics or game controls

------------------------------------------------------------------------

## License

MIT License
