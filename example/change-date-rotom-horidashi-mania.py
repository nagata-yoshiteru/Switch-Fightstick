#!/usr/bin/env python3
import argparse
import serial
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('--port', default='COM4')
parser.add_argument('--count', default=0)
args = parser.parse_args()

def send(msg, duration=0):
    print(msg.replace('Button ', '').replace('HAT ', ''), end=' ', flush=True)
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

def change_date():
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
    send('LY MAX', 1.25)
    sleep(0.038)
    send('Button A', 0.09)
    sleep(0.1)
    send('LY MAX', 0.55)
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
    sleep(2)

def do_rotom():
    send('Button A', 0.05)
    sleep(0.4)
    send('Button A', 0.05)
    sleep(0.4)
    send('HAT BOTTOM', 0.15)
    sleep(0.2)
    for i in range(0,5):
        send('Button A', 0.05)
        sleep(0.038)
    for i in range(0,10):
        send('Button B', 0.05)
        sleep(0.038)
    for i in range(0,20):
        send('Button A', 0.05)
        sleep(0.038)
    for i in range(0,100):
        send('Button B', 0.05)
        sleep(0.038)

def do_horidashi():
    for i in range(0,50):
        send('Button A', 0.05)
        sleep(0.038)
    for i in range(0,50):
        send('Button B', 0.05)
        sleep(0.038)

def do_mania():
    for i in range(0,45):
        send('Button A', 0.05)
        sleep(0.038)
    for i in range(0,20):
        send('Button B', 0.05)
        sleep(0.038)


ser = serial.Serial(args.port, 9600)
n = 0

try:
    while True:
        send('LY MIN', 0.9)   
        sleep(0.05)
        send('LX MIN', 0.4)
        sleep(0.4)
        
        do_rotom()
        change_date()
        do_rotom()

        send('LX MAX', 0.35)
        sleep(0.05)
        send('LY MAX', 1.5)   
        sleep(1.5)
        send('LX MIN', 2)
        sleep(0.4)
        send('LY MAX', 0.45)   
        sleep(0.05)
        send('LX MIN', 1.15)
        sleep(0.05)
        send('LY MIN', 0.5)
        sleep(0.05)

        do_mania()

        send('LY MAX', 0.15)   
        sleep(0.05)
        send('LX MAX', 0.2)
        sleep(0.05)
        send('LY MIN', 0.15)
        sleep(0.05)

        do_horidashi()
        change_date()
        do_horidashi()

        send('LX MIN', 0.25)
        sleep(0.05)
        send('LY MIN', 0.2)
        sleep(0.05)

        do_mania()

        send('LY MAX', 0.2)   
        sleep(0.05)
        send('LX MAX', 2.7)
        sleep(0.05)
        send('LY MIN', 1.5)
        sleep(1.5)

        print(' ')
        n += 1
        if n == int(args.count):
            send('RELEASE')
            ser.close()
            break

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
