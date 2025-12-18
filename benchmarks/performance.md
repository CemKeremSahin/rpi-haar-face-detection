# Performance Benchmark

This document reports the measured performance of the real-time face detection application on Raspberry Pi. All measurements were taken on real hardware under controlled conditions.

---

## Test Environment

- **Device**: Raspberry Pi 3 Model B+
- **CPU**: Broadcom BCM2837B0 (Quad-core ARM Cortex-A53)
- **RAM**: 1 GB
- **Camera**: Pi Camera v1.3 (clone)
- **OS**: Raspberry Pi OS (Trixie)
- **Python**: 3.x
- **OpenCV**: System-installed (`python3-opencv`)
- **Detection Method**: Haar Cascade (frontal face)
- **Resolution**: 640x480 (BGR888)

---

## Measurement Methodology

- FPS is calculated over **1-second windows** and averaged over multiple intervals
- Two modes were evaluated:
  - **GUI Mode**: `cv2.imshow()` enabled (VNC display)
  - **Headless Mode**: No frame rendering, terminal output only
- CPU usage was observed using `top` during execution
- Measurements were repeated to ensure consistency

---

## Results

### GUI Mode (VNC Enabled)

- **Average FPS**: 9–11 FPS
- **CPU Usage**: \~75–85%

### Headless Mode (No Display)

- **Average FPS**: 13–16 FPS
- **CPU Usage**: \~65–75%

---

## Observations

- GUI rendering introduces a noticeable performance penalty
- Haar Cascade performance is highly sensitive to lighting conditions
- Picamera2 provides stable frame acquisition compared to OpenCV VideoCapture

---

## Notes

- Results may vary depending on lighting, camera quality, and background complexity
- These benchmarks reflect real-time performance without hardware acceleration

##



