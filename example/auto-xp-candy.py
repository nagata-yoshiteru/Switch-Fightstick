#!/usr/bin/env python3
import argparse
import serial
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('--port', default='COM4')
args = parser.parse_args()
ser = serial.Serial(args.port, 9600)

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
        send('Button A', 0.1)
        sleep(3)
        send('LY MAX', 0.1)
        sleep(1.2)
        send('Button A', 0.1)
        sleep(1.2)
        send('Button A', 0.1)
        sleep(1.2)
        send('Button A', 0.1)
        sleep(1.2)
        send('Button A', 0.1)
        sleep(3)
        send('Button B', 0.1)
        sleep(3)
        send('Button B', 0.1)
        sleep(1.2)
        send('LY MAX', 0.1)
        sleep(1.2)
        send('Button L', 0.1)
        sleep(1.2)
        print(' ')
except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
