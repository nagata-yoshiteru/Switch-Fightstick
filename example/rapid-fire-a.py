#!/usr/bin/env python3
import argparse
import serial
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('--port', default='COM4')
args = parser.parse_args()

def send(msg, duration=0):
    # print('A', end='', flush=True)
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)

print("Start Rapid Fire Ⓐ ！")
try:
    while True:
        sleep(0.02)
        send('Button A', 0.02)
except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
