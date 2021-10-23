#!venv/Scripts/python

""" Change Windows Volume when a button is pressed in the Pico
"""
from pynput.keyboard import Controller, Key

import serial
import time
import serial.tools.list_ports as port_list

has_pico = False
pico_port = ""
while not has_pico:
    print("Trying to connect")
    for port in port_list.comports():
        if port.vid == 0x2E8A:  # Raspberry vendorId
            print("pico found")
            has_pico = True
            pico_port = port.name
            break
    if not has_pico:
        print("Not found")
        time.sleep(1)

PICO = serial.Serial(pico_port, 9600)
KEYBOARD = Controller()

if __name__ == "__main__":
    while True:
        if pico_data := PICO.read():
            pico_data = pico_data.decode("utf-8")
            print(pico_data)

        if pico_data == "U":
            print("up")
            # Increase volume
            KEYBOARD.press(Key.media_volume_up)
            KEYBOARD.release(Key.media_volume_up)
        elif pico_data == "D":
            print("down")
            # Decrease volume
            KEYBOARD.press(Key.media_volume_down)
            KEYBOARD.release(Key.media_volume_down)
        elif pico_data == "C":
            print("change")
            # Change audio device
            # Needs SoundSwitch to work <https://soundswitch.aaflalo.me/>
            for k in [Key.ctrl, Key.alt, Key.f11]:
                KEYBOARD.press(k)
            for k in [Key.ctrl, Key.alt, Key.f11]:
                KEYBOARD.release(k)