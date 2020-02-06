#!/usr/bin/env python3
import argparse
import serial
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('--port', default='COM4')
parser.add_argument('--mode', default='safe')
args = parser.parse_args()

def send(msg, duration=0):
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

CTRL_C = 3
BS = 8
ENTER = 13
ESC = 27
 
try:
    from msvcrt import getch
except ImportError:
    def getch():
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

if args.mode == 'active':
    ser = serial.Serial(args.port, 9600)
 
while True:
    key = ord(getch())
    if key == CTRL_C:
        if args.mode == 'active':
            ser.close()
        break
    else:
        try:
            if args.mode == 'safe':
                ser = serial.Serial(args.port, 9600)
            ckey = chr(key)
            if key == ENTER or ckey == 'a' or ckey == 'A':
                send('Button A', 0.04)
                print('A', end=' ', flush=True)
            elif key == BS or key == ESC or ckey == 'b' or ckey == 'B':
                send('Button B', 0.04)
                print('B', end=' ', flush=True)
            elif ckey == 'x' or ckey == 'X':
                send('Button X', 0.04)
                print('X', end=' ', flush=True)
            elif ckey == 'y' or ckey == 'Y':
                send('Button Y', 0.04)
                print('Y', end=' ', flush=True)
            elif ckey == 'l' or ckey == 'L':
                send('Button L', 0.04)
                print('L', end=' ', flush=True)
            elif ckey == 'r' or ckey == 'R':
                send('Button R', 0.04)
                print('R', end=' ', flush=True)
            elif ckey == 'h':
                send('Button HOME', 0.04)
                print('H', end=' ', flush=True)
            elif ckey == 'H':
                send('Button HOME', 1.0)
                print('H-', end=' ', flush=True)
            elif ckey == '+' or ckey == ';':
                send('Button SELECT', 0.04)
                print('+', end=' ', flush=True)
            elif ckey == '-' or ckey == '=':
                send('Button START', 0.04)
                print('-', end=' ', flush=True)
            elif ckey == 'z' or ckey == 'Z':
                key = ord(getch())
                ckey = chr(key)
                if ckey == 'l' or ckey == 'L':
                    send('Button ZL', 0.04)
                    print('ZL', end=' ', flush=True)
                elif ckey == 'r' or ckey == 'R':
                    send('Button ZR', 0.04)
                    print('ZR', end=' ', flush=True)
            elif key == 0:
                key = ord(getch())
                ckey = chr(key)
                if ckey == 'H':
                    send('LY MIN', 0.04)
                    print('△', end=' ', flush=True)
                elif ckey == 'P':
                    send('LY MAX', 0.04)
                    print('▽', end=' ', flush=True)
                elif ckey == 'K':
                    send('LX MIN', 0.04)
                    print('◁', end=' ', flush=True)
                elif ckey == 'M':
                    send('LX MAX', 0.04)
                    print('▷', end=' ', flush=True)
                else:
                    print('\n<---->')
                    print(key)
                    print('------')
                    print(ckey)
                    print('>----<')
            elif ckey == 'i' or ckey == 'I':
                send('HAT TOP', 0.04)
                print('▲', end=' ', flush=True)
            elif ckey == 'm' or ckey == 'M':
                send('HAT BOTTOM', 0.04)
                print('▼', end=' ', flush=True)
            elif ckey == 'j' or ckey == 'J':
                send('HAT LEFT', 0.04)
                print('◀', end=' ', flush=True)
            elif ckey == 'k' or ckey == 'K':
                send('HAT RIGHT', 0.04)
                print('▶', end=' ', flush=True)
            elif ckey == 'o' or ckey == 'O':
                send('HAT TOP_RIGHT', 0.04)
                print('◥', end=' ', flush=True)
            elif ckey == ',':
                send('HAT BOTTOM_RIGHT', 0.04)
                print('◢', end=' ', flush=True)
            elif ckey == 'n' or ckey == 'N':
                send('HAT BOTTOM_LEFT', 0.04)
                print('◣', end=' ', flush=True)
            elif ckey == 'u' or ckey == 'U':
                send('HAT TOP_LEFT', 0.04)
                print('◤', end=' ', flush=True)
            else:
                print('\n<---->')
                print(key)
                print('------')
                print(ckey)
                print('>----<')
            if args.mode == 'safe':
                ser.close()
        except serial.serialutil.SerialException:
            print('#E', end='', flush=True)
