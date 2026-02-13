import cv2
import serial
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("Failed ")
    exit()

cap = cv2.VideoCapture(0)
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=0.1)
time.sleep(2)

def send_coord(x, y):
    try:
        message = f"{x},{y}\n"
        arduino.write(message.encode())
        print(f"sent X:{x} Y:{y}")
    except serial.SerialException as e:
        print("send failed:", e)
while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 0), 2)
        centerx = x + w // 2
        centery = y + h // 2

  
        servox = int(centerx * 120 / 640 + 30)
        servoy = int(centery * 120 / 480 + 30)


    cv2.imshow('Video', frame)
    if cv2.waitKey(20) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()
