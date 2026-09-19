import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
while True:

    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.15)
  
    led.value = True
    time.sleep(1)
    led.value = False
    
    time.sleep(0.5)

