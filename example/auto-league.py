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
        sleep(0.04)
        send('Button A', 0.04)
        sleep(0.04)
        send('Button A', 0.04)
        sleep(0.04)
        send('Button A', 0.04)
        sleep(0.04)
        send('Button A', 0.04)
        sleep(0.04)
        send('Button A', 0.04)
        sleep(0.04)
        send('LY MIN', 0.56)
        sleep(0.04)
        send('Button A', 0.04)
        sleep(0.04)
        send('Button A', 0.04)
        sleep(0.04)
        send('Button A', 0.04)
        sleep(0.04)
        send('Button A', 0.04)
        sleep(0.04)
        send('Button A', 0.04)
        sleep(0.04)
        send('Button B', 0.04)
except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
