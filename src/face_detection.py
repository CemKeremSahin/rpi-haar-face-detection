import time

import cv2

from picamera2 import Picamera2





print("Kamera baslatiliyor... (Cikis icin 'q')")

picam2 = Picamera2()





config = picam2.create_video_configuration(main={"size": (640, 480), "format": "BGR888"})

picam2.configure(config)

picam2.start()




face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')





while True:



    frame = picam2.capture_array()



   

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    

    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))



    

    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)





    cv2.imshow('Picamera2 Yuz Takibi', frame)



    

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break



picam2.stop()

cv2.destroyAllWindows()

