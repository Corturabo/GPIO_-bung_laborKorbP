from gpiozero import LED
from time import sleep

led = LED(18)

while True:
    
    led.on()
    sleep(0.25)  

    
    led.off()
    sleep(0.25)  

