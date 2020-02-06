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

print("Start Slow Fire Ⓐ ！")
try:
    while True:
        sleep(1)
        send('Button A', 1)
except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
