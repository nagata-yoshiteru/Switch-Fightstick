#!/usr/bin/env python3
import argparse
import serial
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('--port', default='COM4')
args = parser.parse_args()

def send(msg, duration=0):
    print(msg.replace('Button ', '').replace('HAT ', ''), end=' ', flush=True)
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)

try:
    while True:
        send('Button HOME', 0.09)
        sleep(0.5)
        send('HAT BOTTOM', 0.09)
        sleep(0.038)
        send('HAT RIGHT', 0.09)
        sleep(0.038)
        send('HAT RIGHT', 0.09)
        sleep(0.038)
        send('HAT RIGHT', 0.09)
        sleep(0.038)
        send('HAT RIGHT', 0.09)
        sleep(0.038)
        send('Button A', 0.09)
        sleep(0.8)
        send('LY MAX', 1.2)
        sleep(0.038)
        send('Button A', 0.09)
        sleep(0.1)
        send('LY MAX', 0.5)
        sleep(0.038)
        send('Button A', 0.09)
        sleep(0.15)
        send('HAT BOTTOM', 0.09)
        sleep(0.038)
        send('HAT BOTTOM', 0.09)
        sleep(0.038)
        send('Button A', 0.09)
        sleep(0.3)
        send('HAT RIGHT', 0.09)
        sleep(0.038)
        send('HAT RIGHT', 0.09)
        sleep(0.038)
        send('HAT TOP', 0.09)
        sleep(0.038)
        send('HAT RIGHT', 0.09)
        sleep(0.038)
        send('HAT RIGHT', 0.09)
        sleep(0.038)
        send('HAT RIGHT', 0.09)
        sleep(0.038)
        send('Button A', 0.09)
        sleep(0.3)
        send('Button HOME', 0.09)
        sleep(0.5)
        send('Button HOME', 0.09)
        sleep(1)
        print(' ')
except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
