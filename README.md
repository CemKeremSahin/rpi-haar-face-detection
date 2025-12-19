# Real-Time Face Detection on Raspberry Pi (Picamera2 + OpenCV)

## Overview

This repository is a **continuation and refinement** of a basic face detection experiment on Raspberry Pi. It focuses on turning a working demo into a **reproducible, benchmarked, and CV-ready embedded computer vision project**.

The application performs real-time face detection using **Picamera2** (libcamera-based camera stack) and **OpenCV Haar Cascades**, with explicit attention to embedded constraints such as CPU load, camera stability, and resolution trade-offs.

---

## Key Features

- Direct camera access via **Picamera2** (avoids VideoCapture instability)
- Real-time face detection using OpenCV
- FPS measurement for performance evaluation
- Designed for Raspberry Pi 3 


---

## Hardware & Software Requirements

### Hardware

- Raspberry Pi 3&#x20;
- Raspberry Pi Camera (v1.3 or compatible clone)

### Software

- Raspberry Pi OS (Bullseye or newer)
- Python 3.x
- Git

---

## Installation

### 1. Enable Camera Interface

```bash
sudo raspi-config
```

Navigate to:

- Interface Options → Camera → Enable

Reboot the system after enabling the camera.

---

### 2. Clone the Repository

```bash
git clone https://github.com/CemKeremSahin/rpi-haar-face-detection.git
cd rpi-face-detection
```

---

### 3. Install Dependencies

Update system packages:

```bash
sudo apt update
```

Install OpenCV (system package recommended on Raspberry Pi):

```bash
sudo apt install python3-opencv
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
rpi-haar-face-detection/
│
├── src/
│   └── face_detection.py           # Main application
├── models/
│   └── haarcascade_frontalface_default.xml
├── requirements.txt
├── README.md
├── benchmarks/
│   └── performance.md              # FPS and CPU usage results
```

---

## How It Works

1. Initialize the Raspberry Pi camera using Picamera2 with a BGR888 video configuration
2. Capture frames as NumPy arrays
3. Convert frames to grayscale
4. Detect faces using Haar Cascade classifiers
5. Draw bounding boxes 


---

## Running the Application

```bash
python3 src/face_detection.py
```

Press **q** to exit the application.

---

## Performance Benchmarking

- FPS is measured over 1-second windows
- Both GUI-enabled and headless modes are supported
- Benchmark results are documented in:

```
benchmarks/performance.md
```

---

## Limitations

- Haar Cascade performance degrades under poor lighting
- CPU-bound processing (no hardware acceleration)
- No face recognition or tracking persistence

---

## Future Improvements

- Replace Haar Cascade with DNN-based face detectors
- Integrate TensorFlow Lite or MediaPipe
- Add CPU and memory usage logging
- Enable headless streaming over network

---

## Skills Demonstrated

- Embedded Linux development on Raspberry Pi
- Camera stack integration (libcamera / Picamera2)
- Real-time image processing with OpenCV
- Performance-aware system design
- Benchmarking and reproducibility

---

## Author Note

This project is intended as a **portfolio-ready embedded computer vision example**, emphasizing correct system integration and measurable performance rather than purely algorithmic complexity.

