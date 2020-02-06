# Switch-Fightstick
[![Thumbnail](https://i.imgur.com/cJLZUdhl.jpg)](https://twitter.com/ebith/status/954858876028907521)
- [Xenoblade Chronicles 2](https://twitter.com/ebith/status/954858876028907521)
- [Octopath Traveler](https://twitter.com/ebith/status/1079163336862818305)

## Requirement
- ATMega32U4 Board or see [shinyquagsire23/Switch-Fightstick's README](https://github.com/shinyquagsire23/Switch-Fightstick/blob/master/README.md)
- USB to serial adapter
- USB micro-b cable * 2

## Usage
[NintendoSwitchをPCから操作する - おいら屋ファクトリー](https://blog.feelmy.net/control-nintendo-switch-from-computer/)(in Japanese)

### On MacOS
```sh
brew install avrdude osx-cross/avr/avr-gcc
git clone --recursive https://github.com/ebith/Switch-Fightstick.git
cd Switch-Fightstick
make
avrdude -pm32u4 -cavr109 -D -P$(ls /dev/tty.usbmodem*) -b57600 -Uflash:w:Joystick.hex # need reset

pip3 install pyserial
./example/rapid-fire-a.py /dev/tty.usbserial*
```

### On Windows
1. Install Arduino IDE
2. Add `C:\Program Files (x86)\Arduino\hardware\tools\avr\bin` to your environment PATH.
3. Run following. COMx : ex. COM4 -> x = 4
```cmd
git clone --recursive https://github.com/ebith/Switch-Fightstick.git
cd Switch-Fightstick
make
avrdude -pm32u4 -cavr109 -D -P COMx -b57600 -Uflash:w:Joystick.hex # need reset

pip3 install pyserial
./example/rapid-fire-a.py COMx
```
