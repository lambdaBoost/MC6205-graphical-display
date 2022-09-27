from machine import Pin, SPI
import rp2
from time import sleep, sleep_us, sleep_us


import machine


CATHODE_PULSE_WIDTH = 1
CATHODE_HOLD_TIME = 5
BLANKING_INTERVAL = 1

group_cathode_clk = Pin(6, Pin.OUT)
group_cathode_rst = Pin(5, Pin.OUT)
individual_cathode_clk = Pin(4, Pin.OUT)
individual_cathode_rst = Pin(3, Pin.OUT)


    

@rp2.asm_pio(
    set_init=rp2.PIO.OUT_LOW,
    out_init=rp2.PIO.OUT_LOW,
    sideset_init=rp2.PIO.OUT_LOW,
    autopull=False
)
def matrix_row():
    """
    Send 32 bits to the DATA pin and latch
    """
    pull()
    label('reset_x1')
    set(x, 31)                       # loop counter, loop 16 times
    label('bitloop1')
    out(pins, 1)       .side(1)      # {1} mov 1bit to DATA pin
                                     #     and set CLOCK high
    jmp(x_dec, 'delay1')              # {2} jump to 'delay'
    
    pull()
    set(x, 31)                       # loop counter, loop 16 times
    label('bitloop2')
    out(pins, 1)       .side(1)      # {1} mov 1bit to DATA pin
                                     #     and set CLOCK high
    jmp(x_dec, 'delay2')              # {2} jump to 'delay'
    
    pull()
    set(x, 31)                       # loop counter, loop 16 times
    label('bitloop3')
    out(pins, 1)       .side(1)      # {1} mov 1bit to DATA pin
                                     #     and set CLOCK high
    jmp(x_dec, 'delay3')              # {2} jump to 'delay'
    
    
    set(pins, 1)                     # {3} set LATCH high
    set(x, 31)         .side(0)   [2]   # {4} reset counter
    set(pins, 0)                     # {5} set LATCH low
    jmp('reset_x1')                   # {6} restart loop

    
    label('delay1')
    nop()                            # {3}
    jmp('bitloop1')     .side(0)  [2] # {4-6}    
    
    label('delay2')
    nop()                            # {3}
    jmp('bitloop2')     .side(0)  [2] # {4-6}
    
    label('delay3')
    nop()                            # {3}
    jmp('bitloop3')     .side(0)  [2] # {4-6}    


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
    set(y, 2)         .side(0)   [2]   # {4} reset counter
    set(pins, 0)                     # {5} set LATCH low
    #set(y, 2)
    jmp('reset_x')                   # {6} restart loop

    
    label('delay')
    nop()                            # {3}
    jmp('bitloop')     .side(0)  [2] # {4-6}
    
    #label('setup')
    #set(y,2)
    #jmp('reset_x')
    

    



"""
def latch_row():

    wrap_target()
    set(pins, 1)  [6]                   # {3} set LATCH high
    set(pins, 0)                     # {5} set LATCH low
  
    
"""   
sm0 = rp2.StateMachine(0, matrix_row_2, freq=1000000,
                      sideset_base=Pin(2),    # CLOCK pin
                      set_base=Pin(1),        # LATCH pin
                      out_base=Pin(0),        # DATA pin
                     )

"""
sm1 = rp2.StateMachine(1, latch_row, freq=100000,
                      sideset_base=Pin(2),    # CLOCK pin
                      set_base=Pin(1),        # LATCH pin
                      out_base=Pin(0),        # DATA pin
                     )
                     
"""

"""
sm2 = rp2.StateMachine(2, latch_row, freq=100000,
                      sideset_base=Pin(2),    # CLOCK pin
                      set_base=Pin(1),        # LATCH pin
                      out_base=Pin(0),        # DATA pin
                     )
"""


sm0.active(1)
#sm0.put(0b11111111111111111111111111111111)
#sm0.exec("set(y, 2)")

while True:
    
    #sm0.exec("set(y, 2)")
    
    for i in range(10):
        group_cathode_clk.value(1)
        sleep_us(CATHODE_PULSE_WIDTH)
        group_cathode_clk.value(0)
        #sleep_us(CATHODE_HOLD_TIME)
        
        
        
        for j in range(10):
            individual_cathode_clk.value(1)
            sleep_us(CATHODE_PULSE_WIDTH)
            individual_cathode_clk.value(0)
            #value = 2863311530 #32 bit decimal for alternating 1s and 0s
            
            #sm.restart()
            
            if j % 2 ==0:
                #value = 2863311530 #10 pattern
                value = 0b01010101010101010101010101010101
            else:
                value = 0b10101010101010101010101010101010
                #value = 1431655765 #alternating 10 pattern
            #value = 0b11111111111111111111111111111111
            sm0.put(value)
            sm0.put(0b11111111111111111111111111111111)
            sm0.put(value)
            
            #sm0.active(1)
            #sm0.active(0)
            

            

            


        
    



