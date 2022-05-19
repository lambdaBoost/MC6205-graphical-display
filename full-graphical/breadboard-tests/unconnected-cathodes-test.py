#testing cathodes connected via decade counters to ground
#most reliable way to ensure non-connected cathodes light

from machine import Pin
from time import sleep, sleep_us

rst = Pin(0, Pin.OUT, value=0)
clk = Pin(1, Pin.OUT, value=0)
group_rst = Pin(2, Pin.OUT, value=0)
group_clk = Pin(3, Pin.OUT, value=0)



while True:
    #00
    sleep(1)
            
    clk.value(1)
    sleep_us(10)
    clk.value(0)
    
    #01
    sleep(1)
    
    rst.value(1)
    sleep_us(10)
    rst.value(0)
    
    group_clk.value(1)
    sleep_us(10)
    group_clk.value(0)
    
    #10
    sleep(1)
    
    clk.value(1)
    sleep_us(10)
    clk.value(0)
    
    #11
    sleep(1)
    
    rst.value(1)
    group_rst.value(1)
    sleep_us(10)
    rst.value(0)
    group_rst.value(0)
    
    
