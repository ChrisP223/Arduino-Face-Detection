import serial
import time
#test to see if theres a problem with serial communication
arduino = serial.Serial('COM3', 115200, timeout=.1)
time.sleep(2)

for i in range(90, 120, 5):
    arduino.write(f"{i},{90}\n".encode())
    time.sleep(0.05) 
