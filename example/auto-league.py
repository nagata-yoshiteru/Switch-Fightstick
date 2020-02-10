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
        for i in range(0,14):
            send('Button A', 0.04)
            sleep(0.04)
        sleep(0.24)
        send('LY MIN', 0.55)
        sleep(0.04)
        # send('Button A', 0.04)
        # sleep(0.04)
        # send('Button B', 0.04)
        # sleep(0.04)
        # send('Button B', 0.04)
        # sleep(0.04)
        # send('Button B', 0.04)
        # sleep(0.04)
        print(' ')
except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
