#!/usr/bin/env python3
import argparse
import serial
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('--port', default='COM4')
args = parser.parse_args()

def send(msg, duration=0):
    print(msg)
    ser.write(f'{msg}\r\n'.encode('utf-8'));
    sleep(duration)
    ser.write(b'RELEASE\r\n');

ser = serial.Serial(args.port, 9600)

try:
    while True:
        sleep(1.2)
        send('Button ZL', 0.1)
        sleep(3)
        send('Button A', 0.1)
        sleep(1.2)
        send('Button A', 0.1)
        sleep(1.2)
        send('Button B', 0.1)
        sleep(1.2)
        send('LY MIN', 0.1)
        sleep(1.2)
        send('Button ZL', 0.1)
        sleep(3)
        send('Button A', 0.1)
        sleep(1.2)
        send('Button ZL', 0.1)
        sleep(3)
        send('Button A', 0.1)
        sleep(1.2)
        send('LY MIN', 0.1)
        sleep(1.2)
        send('Button ZL', 0.1)
        sleep(3)
        send('Button A', 0.1)
        sleep(1.2)
        send('LY MIN', 0.1)
        sleep(1.2)
        send('Button ZL', 0.1)
        sleep(3)
        send('Button L', 0.1)
        sleep(0.1)
        send('Button L', 0.1)
        sleep(1.2)
except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
