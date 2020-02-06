import serial
from time import sleep

port = "COM4"

def send(msg, duration=0):
    print(msg)
    ser.write(f'{msg}\r\n'.encode('utf-8'));
    sleep(duration)
    ser.write(b'RELEASE\r\n');

ser = serial.Serial(port, 9600)

send('Button A', 0.04)
