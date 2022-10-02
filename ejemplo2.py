from machine import Pin, Timer #importing pin, and timer class

led = Pin(25, Pin.OUT)  #GPIO25 as led output
led.value(0)            #LED is off

timer = Timer(period=5000, mode=Timer.PERIODIC, callback=lambda t:print("Welcome to VEGA07-SLIM")) #Timer initialization
