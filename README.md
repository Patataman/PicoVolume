# PicoVolume

Add multimedia buttons to your keyboard!



## Systems

- Windows
- Linux (In a future, probably when Steam Deck is released)
. MaacOS, HAHAHAHAHAH

## Windows' external dependencies

- [SoundSwitch](https://soundswitch.aaflalo.me/): For being able to easily switch between audiodevices

## How it works

The "program" use 2 scripts:

1. main-pico.py

This program runs on the Raspberry Pico and its the one to detect when a button is pressed and send to the computer, with a print through the standard output, which button is pressed.

2. main-windows.py

This programs run on the computer and its the one in charge to detect and connect to the Raspberry Pico through a serial port and to make the desired change. At this moment there are 3 possible actions:

-- Volume Up, identified with the letter U
-- Volume Down, identified with the letter D
-- Change Audio Device, identified with the letter C