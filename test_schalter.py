from gpiozero import LED,Button
import time

button=Button(24,pull_up=True)

led1 = LED(18)
led2 = LED(22)

led_state = False

while True:
    
    if button.is_pressed:
        led_state = not led_state
        led1.value = led_state
        led2.value = not led_state
        time.sleep(0.1)  
  

