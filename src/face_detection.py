import time

import cv2

from picamera2 import Picamera2



# 1. Picamera2'yi Başlat (OpenCV Yerine Bunu Kullanıyoruz)

# Bu kütüphane yeni Raspberry Pi OS ile tam uyumludur.

print("Kamera baslatiliyor... (Cikis icin 'q')")

picam2 = Picamera2()



# 2. Ayarlar (Bellek dostu 640x480 çözünürlük ve OpenCV için BGR formatı)

config = picam2.create_video_configuration(main={"size": (640, 480), "format": "BGR888"})

picam2.configure(config)

picam2.start()



# 3. Yüz Tanıma Modelini Yükle

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



# 4. Sonsuz Döngü

while True:

    # Kameradan görüntüyü "Numpy Array" olarak al (OpenCV formatı)

    # Bu komut VideoCapture(0)'dan çok daha hızlı ve stabildir.

    frame = picam2.capture_array()



    # Gri tona çevir

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    # Yüzleri bul

    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))



    # Kare çiz

    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)



    # Ekranda göster

    cv2.imshow('Picamera2 Yuz Takibi', frame)



    # 'q' ile çık

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break



picam2.stop()

cv2.destroyAllWindows()

