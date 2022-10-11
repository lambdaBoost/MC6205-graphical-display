#TODO:
#increase group count from 8 to 10 when new cathodes are connected

from machine import Pin, SPI
import rp2
from time import sleep, sleep_us, sleep_us
import json
import anode_write
import network
import machine

from anode_write import anode_order, get_api_image
from secrets import secrets


try:
  import usocket as socket
except:
  import socket
  
  
ssid = secrets['ssid']
pw = secrets['pw']

URI = "http://192.168.1.215:8080"


wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(ssid, pw)

timeout = 10
while timeout > 0:
    if wlan.status() >= 3:
        break
    timeout -= 1
    print('Waiting for connection...')
    sleep(1)
   
wlan_status = wlan.status()


CATHODE_PULSE_WIDTH = 1
CATHODE_HOLD_TIME = 10
BLANKING_INTERVAL = 1

group_cathode_clk = Pin(6, Pin.OUT)
group_cathode_rst = Pin(5, Pin.OUT)
individual_cathode_clk = Pin(4, Pin.OUT)
individual_cathode_rst = Pin(3, Pin.OUT)

#test image for now
#display_image = anode_write.read_test_file()
display_image = get_api_image(URI+"/test_image/")



@rp2.asm_pio(
    set_init=rp2.PIO.OUT_LOW,
    out_init=rp2.PIO.OUT_LOW,
    sideset_init=rp2.PIO.OUT_LOW,
    autopull=True
)
def matrix_row_2():
    """
    Send 4 bytes (32 bits) to the DATA pin,
    one bit per cycle. Then create a pulse on
    the LATCH pin to display the 32 bits.
    """

    #jmp(not_y, 'setup')				#when initialising set y to 2
    
    label('reset_x')
    #pull()
    set(x, 31)                       # loop counter, loop 16 times
    label('bitloop')
    out(pins, 1)       .side(1)      # {1} mov 1bit to DATA pin
                                     #     and set CLOCK high
    jmp(x_dec, 'delay')              # {2} jump to 'delay'
    jmp(y_dec,'reset_x')
    
    set(pins, 1)                     # {3} set LATCH high
    set(y, 3)         .side(0)   [2]   # {4} reset counter
    set(pins, 0)                     # {5} set LATCH low
    nop()								#delay for blanking operation
    nop()
    #set(y, 2)
    jmp('reset_x')                   # {6} restart loop

    
    label('delay')
    nop()                            # {3}
    jmp('bitloop')     .side(0)  [2] # {4-6}
    
    #label('setup')
    #set(y,2)
    #jmp('reset_x')
    

    


  
sm0 = rp2.StateMachine(0, matrix_row_2, freq=5000000,
                      sideset_base=Pin(2),    # CLOCK pin
                      set_base=Pin(1),        # LATCH pin
                      out_base=Pin(0),        # DATA pin
                     )



sm0.active(1)
sm0.exec("set(y, 3)")


group_cathode_rst.value(1)
sleep_us(CATHODE_PULSE_WIDTH)
group_cathode_rst.value(0)

individual_cathode_rst.value(1)
sleep_us(CATHODE_PULSE_WIDTH)
individual_cathode_rst.value(0)


while True:
    
    anode_count = 0
    #sm0.exec("set(y, 2)")
    
    #TODO - only counts 8 groups for now. Remember to increase when missing cathode are connected
    for i in range(10):
        if i>0:
            group_cathode_clk.value(1)
            sleep_us(CATHODE_PULSE_WIDTH)
            group_cathode_clk.value(0)
        #sleep_us(CATHODE_HOLD_TIME)
        
        
        
        for j in range(10):
            
            anode_num = anode_order[anode_count]
            row = display_image[anode_num]
            
            if j > 0:
                individual_cathode_clk.value(1)
                sleep_us(CATHODE_PULSE_WIDTH)
                individual_cathode_clk.value(0)


            sm0.put(row[0])          
            sm0.put(row[1])
            sm0.put(row[2])
            sm0.put(row[3])



            sleep_us(CATHODE_HOLD_TIME)
            
            #blanking - do before data to shorten delay
            #sm0.put(0b000000000000000000000000000000)
            #sm0.put(0b000000000000000000000000000000)
            #sm0.put(0b000000000000000000000000000000)
            #sm0.put(0b000000000000000000000000000000)
            #sleep_us(BLANKING_INTERVAL)

            anode_count = anode_count + 1
            

            

            #sm0.active(0)
            
        individual_cathode_rst.value(1)
        sleep_us(CATHODE_PULSE_WIDTH)
        individual_cathode_rst.value(0)
        
    group_cathode_rst.value(1)
    sleep_us(CATHODE_PULSE_WIDTH)
    group_cathode_rst.value(0)

            


        
 