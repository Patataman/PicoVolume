""" Send data to Windows when a button is pressed
"""

from machine import Pin
import time

DELAY = time.ticks_ms()
DELAY_MS = 250

def more_volume(inst):
    global DELAY, DELAY_MS
    
    if time.ticks_diff(time.ticks_ms(), DELAY) < DELAY_MS:
        return

    print("U")
    DELAY = time.ticks_ms()
    
def less_volume(inst):
    global DELAY, DELAY_MS
    
    if time.ticks_diff(time.ticks_ms(), DELAY) < DELAY_MS:
        return

    print("D")
    DELAY = time.ticks_ms()
    
def change_device(inst):
    global DELAY, DELAY_MS
    
    if time.ticks_diff(time.ticks_ms(), DELAY) < DELAY_MS:
        return

    print("C")
    DELAY = time.ticks_ms()


but1 = Pin(4, Pin.IN, Pin.PULL_DOWN)
but2 = Pin(3, Pin.IN, Pin.PULL_DOWN)
but3 = Pin(2, Pin.IN, Pin.PULL_DOWN)

but1.irq(handler=more_volume, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
but2.irq(handler=less_volume, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
but3.irq(handler=change_device, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)