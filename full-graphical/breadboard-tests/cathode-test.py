from machine import Pin
import time

X1 = Pin(0, Pin.OUT, value=0)
X2 = Pin(4, Pin.OUT, value=0)
X3 = Pin(2, Pin.OUT, value=0)
X4 = Pin(21, Pin.OUT, value=0)
X5 = Pin(19, Pin.OUT, value=0)
X6 = Pin(5, Pin.OUT, value=0)
X7 = Pin(18, Pin.OUT, value=0)

AD1357 = Pin(23, Pin.OUT, value=0)
AD246 = Pin(22, Pin.OUT, value=0)

CCLK1 = Pin(12, Pin.OUT, value=0)
CCLK2 = Pin(13, Pin.OUT, value=0)

ACLK1 = Pin(27, Pin.OUT, value=0)
ACLK2 = Pin(26, Pin.OUT, value=0)


def setCathode(cathode):
    
    
    CCLK1.value(0)
    
    #counts from 0-15
    X4.value(cathode & 0x1)
    X5.value((cathode & 0x2)>>1)
    X6.value((cathode & 0x4)>>2)
    X7.value((cathode & 0x8)>>3)
    
    #counts from 0-4
    X1.value((cathode & 0x10)>>4)
    X2.value((cathode & 0x20)>>5)
    X3.value((cathode & 0x40)>>6)
    
    CCLK2.value(1)
    time.sleep_us(2)
    CCLK2.value(0)
    
    
    
    CCLK1.value(1)
    time.sleep_us(2)   
    CCLK1.value(0)
    
    #print('cathode set at' + str(cathode & 0x1) + str((cathode & 0x2)>>1) + str((cathode & 0x4)>>2))
    
    
for k in range(40):
                
    AD1357.value(1)
    AD246.value(1)
                
    ACLK1.value(1)
    ACLK2.value(1)

    time.sleep_us(2)
    ACLK1.value(0)
    ACLK2.value(0)

    
    
while True:
    
    for i in range(16):
        for j in range(5):
            

            setCathode(j<<4|i)
            time.sleep_us(200)


            
            
                
                
    