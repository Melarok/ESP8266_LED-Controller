import machine
import time

led = machine.Pin(5, machine.Pin.OUT)

while True:
    led.off()           # Turns the LED on (even though it says led.off)
    time.sleep(1800)    # Time in seconds how long it'll stay on
    led.on()            # Turns the LED off (even though it says led.on)
    time.sleep(1800)    # Time in seconds how long it'll stay off
    #led.off()
    #time.sleep(1800)
    #led.on()
    #time.sleep(1800)

# If you need more complex cycles, uncomment the lines above as needed
