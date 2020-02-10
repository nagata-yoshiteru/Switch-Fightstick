avrdude -C "C:\Program Files (x86)\Arduino\hardware\tools\avr\etc\avrdude.conf" -v -p atmega32u4 -c avr109 -P COM6 -b 57600 -D -U flash:w:Joystick_32u4.hex
