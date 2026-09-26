import time
import board
import digitalio


led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP17)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

print("Button")

while True:
    if not button.value:
        print("Button pressed")
        led.value = True
        time.sleep(1)       
        led.value = False  
        print("LED OFF")
        
    time.sleep(0.05)  
