import cv2
import os.path as path

print(path.isfile("venv/Ressources/Capture4.PNG"))

cap = cv2.VideoCapture(0)

success = True

while success:
    success, img = cap.read()
    cv2.imshow("Video2", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
