from machine import Pin
from time import sleep, sleep_us

A = Pin(0, Pin.OUT, value=0)
B = Pin(1, Pin.OUT, value=0)
C = Pin(2, Pin.OUT, value=0)
D = Pin(3, Pin.OUT, value=0)

b1 = Pin(4, Pin.OUT, value=0)
b2 = Pin(5, Pin.OUT, value=0)
b3 = Pin(6, Pin.OUT, value=0)
b4 = Pin(7, Pin.OUT, value=0)
b5 = Pin(8, Pin.OUT, value=0)
b6 = Pin(9, Pin.OUT, value=0)
b7 = Pin(10, Pin.OUT, value=0)
b8 = Pin(11, Pin.OUT, value=0)



while True:
    
    for b in [b1,b2,b3,b4,b5,b6,b7,b8]:
        
        b.value(1)
        
        
        D.value(0)
        C.value(0)
        B.value(0)
        A.value(0)
            
        sleep_us(10)



        D.value(0)
        C.value(0)
        B.value(0)
        A.value(1)
            
        sleep_us(10)
            
        D.value(0)
        C.value(0)
        B.value(1)
        A.value(0)
            
        sleep_us(10)
            
        D.value(0)
        C.value(0)
        B.value(1)
        A.value(1)
            
        sleep_us(10)
            
        D.value(0)
        C.value(1)
        B.value(0)
        A.value(0)
            
        sleep_us(10)
            
        D.value(0)
        C.value(1)
        B.value(0)
        A.value(1)
            
        sleep_us(10)
            
            
        D.value(0)
        C.value(1)
        B.value(1)
        A.value(0)
            
        sleep_us(10)
            
        D.value(0)
        C.value(1)
        B.value(1)
        A.value(1)
            
        sleep_us(10)
        
            
        D.value(1)
        C.value(0)
        B.value(0)
        A.value(0)
            
        sleep_us(10)
            
        D.value(1)
        C.value(0)
        B.value(0)
        A.value(1)
            
        sleep_us(10)
            
        b.value(0)
            
            
            
            
           
           
