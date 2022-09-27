from machine import Pin, SPI
from time import sleep, sleep_us, sleep_us
from sr_74hc595_spi import SR
from sr_74hc595_bitbang import SR as bitbang_SR

import machine
#led = machine.Pin("LED", machine.Pin.OUT, value=1)
#led.value(1)


CATHODE_PULSE_WIDTH = 5
CATHODE_HOLD_TIME = 200
BLANKING_INTERVAL = 1

group_cathode_clk = Pin(6, Pin.OUT)
group_cathode_rst = Pin(5, Pin.OUT)
individual_cathode_clk = Pin(4, Pin.OUT)
individual_cathode_rst = Pin(3 , Pin.OUT)

anode_ser = Pin(0, Pin.OUT)
anode_srclk = Pin(2, Pin.OUT)
anode_rclk = Pin(1, Pin.OUT)
#oe = Pin(7, Pin.OUT)    # low enables output
#srclr = Pin(8, Pin.OUT) # pulsing low clears data

"""
spi = machine.SPI(0,
                  baudrate=50000,
                  polarity=1,
                  phase=1,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=anode_srclk,
                  #mosi=machine.Pin(7),
                  miso=anode_ser)
"""

"""
sr = SR(spi, anode_rclk, 12)
buf = bytearray(12)
#sr[0] = 0x0000000000000000000000000
for k in range(12):
    sr[k] = 0xaa
    #sr.latch()
"""

bitbang_sr = bitbang_SR(anode_ser, anode_srclk, anode_rclk)

val = 0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
#val = 0b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#val = 0b1
bitbang_sr.bits(val,100)
bitbang_sr.latch()

while True:
    

    
    for i in range(10):
        
        
        group_cathode_clk.value(1)
        sleep_us(CATHODE_PULSE_WIDTH)
        group_cathode_clk.value(0)
            #sleep_us(CATHODE_HOLD_TIME)
        
        
        
        for j in range(10):

            individual_cathode_clk.value(1)
            sleep_us(CATHODE_PULSE_WIDTH)
            individual_cathode_clk.value(0)
            sleep_us(CATHODE_HOLD_TIME)


        individual_cathode_rst.value(1)
        sleep_us(2)
        individual_cathode_rst.value(0)
        
        
    group_cathode_rst.value(1)
    sleep_us(2)
    group_cathode_rst.value(0)
    

            
         

            


        
    



