from cv2 import cv2
import time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    check, frame = video.read()
    faces=face_cascade.detectMultiScale(frame,
                                    scaleFactor=1.05,
                                    minNeighbors=5)
    
    for x, y, w, h in faces:
        frame=cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    #time.sleep(3)
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()