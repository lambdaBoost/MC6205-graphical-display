#test connected cathodes via 2 decade counters - one on the emitters (via transistors) and 1 on the bases

from machine import Pin
from time import sleep, sleep_us

base_cnt = Pin(0, Pin.OUT, value=0)
base_rst = Pin(1, Pin.OUT, value=0)
emitter_cnt = Pin(2, Pin.OUT, value=0)
emitter_rst = Pin(3, Pin.OUT, value=0)

SLEEP_PERIOD = 100

while True:

#step through all 10 emitters with base at zero
    sleep_us(SLEEP_PERIOD)
    
    for i in range(9):
        emitter_cnt.value(1)
        sleep_us(10)
        emitter_cnt.value(0)
        sleep_us(SLEEP_PERIOD)
        
    emitter_rst.value(1)
    sleep_us(10)
    emitter_rst.value(0)
    
    #step through base 1-7
    
    for j in range(7):
        
        base_cnt.value(1)
        sleep_us(10)
        base_cnt.value(0)
        
        sleep_us(SLEEP_PERIOD)
        
        for k in range(9):
            emitter_cnt.value(1)
            sleep_us(10)
            emitter_cnt.value(0)
            sleep_us(SLEEP_PERIOD)
        
        emitter_rst.value(1)
        sleep_us(10)
        emitter_rst.value(0)
    
    base_rst.value(1)
    sleep_us(10)
    base_rst.value(0)
    
