#!/usr/bin/env python3
import argparse
import serial
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('--port', default='COM4')
parser.add_argument('--count', default=0)
args = parser.parse_args()
ser = serial.Serial(args.port, 9600)
n = 0

def send(msg, duration=0):
    global ser
    try:
        ser.write(f'{msg}\r\n'.encode('utf-8'))
        print(msg.replace('Button ', '').replace('HAT ', '').replace('LY MIN', '△ ').replace('LY MAX', '▽ ').replace('LX MIN', '◁').replace('LX MAX', '▷'), end=' ', flush=True)
        sleep(duration)
        ser.write(b'RELEASE\r\n')
    except serial.serialutil.SerialException:
        while True:
            print("Reconnecting... ", end=' ', flush=True)
            try:
                sleep(0.4)
                ser = serial.Serial(args.port, 9600)
                print("Success.")
                sleep(0.1)
                send(msg, duration)
                break
            except:
                print("Faild. Retrying...")

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
        n += 1
        if n == int(args.count):
            send('RELEASE')
            ser.close()
            break

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
