from machine import Pin
from time import sleep, sleep_us

bin_clk = Pin(0, Pin.OUT, value=0)
bin_rst = Pin(1, Pin.OUT, value=0)
dec_clk = Pin(2, Pin.OUT, value=0)
dec_rst = Pin(3, Pin.OUT, value=0)

blank = Pin(4, Pin.OUT, value=1)


while True:
    
    #step through cathodes for zero output on decimat counter
    for j in range(10):
        bin_clk.value(1)
        sleep_us(10)
        bin_clk.value(0)
        sleep_us(100000)
            
    bin_rst.value(1)
    sleep_us(10)
    bin_rst.value(0)
        
    
    for i in range(7):
        
        dec_clk.value(1)
        sleep_us(10)
        dec_clk.value(0)
        
        for j in range(10):
            bin_clk.value(1)
            sleep_us(10)
            bin_clk.value(0)
            sleep_us(100000)
            
        bin_rst.value(1)
        sleep_us(10)
        bin_rst.value(0)
        
    dec_rst.value(1)
    sleep_us(10)
    dec_rst.value(0)
