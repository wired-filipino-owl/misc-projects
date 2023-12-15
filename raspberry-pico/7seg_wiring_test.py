###############################################################
#File:   7seg_wiring_test.py
#Author: Rob Galeoto
#Date:   15 Dec 2023
#Program Description:
#4-digit 7 segment display driven by 74HC595 shift register wiring test
###############################################################

#library includes
from machine import Pin
from utime import sleep_us, sleep_ms, sleep

#global definitions
eight = 0b11111110
dp = 0x1

#pin setup
led_onboard = Pin("LED")
sr_clk = Pin(2, Pin.OUT)
sr_data = Pin(1, Pin.OUT)
seg_digit0 = Pin(13, Pin.OUT)
seg_digit1 = Pin(12, Pin.OUT)
seg_digit2 = Pin(11, Pin.OUT)
seg_digit3 = Pin(10, Pin.OUT)

#function to shift and clock the shift register
#this is slowed down so that we can see the segments illuminate,
#one at a time
def shift_out(sout):
    for i in range(0, 8):
        sr_clk.off()
        sr_data.value((sout >> i) & 0x1)
        sleep_ms(25)
        sr_clk.on()
        sleep_ms(25)
    #clock one more times to propagate value
    sr_clk.off()
    sleep_ms(25)
    sr_clk.on()
    sleep_ms(25)
    sr_clk.off()

#make sure our pins start out turned off
sr_clk.off()
seg_digit0.off()
seg_digit1.off()
seg_digit2.off()
seg_digit3.off()

#test all our segments and digits
#goes in order from segment a to g to dp
#and leftmost digit to rightmost
while True:
    seg_digit0.on()
    shift_out(eight | dp)
    sleep_ms(200)
    seg_digit0.off()
    
    shift_out(0)
    
    seg_digit1.on()
    shift_out(eight | dp)
    sleep_ms(200)
    seg_digit1.off()
    
    shift_out(0)
    
    seg_digit2.on()
    shift_out(eight | dp)
    sleep_ms(200)
    seg_digit2.off()
    
    shift_out(0)
    
    seg_digit3.on()
    shift_out(eight | dp)
    sleep_ms(200)
    seg_digit3.off()
    
    shift_out(0)
