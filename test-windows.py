""" Play with the audio using the keyboard (without Pico)
"""

from pynput.keyboard import Controller, Key

KEYBOARD = keyboard.Controller()

while True:
    val = input("U/D/C: ")
    if val == "U":
        # Increase volume
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
    elif val == "D":
        # Decrease volume
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
    elif val == "C":
        # Change audio device
        # Needs SoundSwitch to work <https://soundswitch.aaflalo.me/>
        for k in [Key.ctrl, Key.alt, Key.f11]:
            KEYBOARD.press(k)
        for k in [Key.ctrl, Key.alt, Key.f11]:
            KEYBOARD.release(k)