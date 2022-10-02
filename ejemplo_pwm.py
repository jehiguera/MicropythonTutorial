#Date:11/05/2022
#Example of PWM with raspberry Pico
#jhiguera@ledmotive.com


from machine import Pin, PWM
from time import sleep

led = PWM(Pin(25))
led.freq(1000)


while True:
    for duty in range(0,65535):
        led.duty_u16(duty)
        sleep(0.0001)