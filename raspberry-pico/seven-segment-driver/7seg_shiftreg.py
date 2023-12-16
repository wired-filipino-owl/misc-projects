###############################################################
#File:   7seg_shiftreg.py
#Author: Rob Galeoto
#Date:   15 Dec 2023
#Program Description:
#4-digit 7 segment display driven by 74HC595 shift register
###############################################################

#library includes
from machine import Pin
from utime import sleep_us, sleep_ms, sleep

#pin setup
led_onboard = Pin("LED")
sr_clk = Pin(2, Pin.OUT)
sr_data = Pin(1, Pin.OUT)
seg_digit0 = Pin(13, Pin.OUT)
seg_digit1 = Pin(12, Pin.OUT)
seg_digit2 = Pin(11, Pin.OUT)
seg_digit3 = Pin(10, Pin.OUT)

#global definitions: encoded seven seg values
test = 0xAA
#logical OR a character with dp to get decimal point on that character
dp = 0x1
zero =  0b11111100
one =   0b01100000
two =   0b11011010
three = 0b11110010
four =  0b01100110
five =  0b10110110
six =   0b10111110
seven = 0b11100000
eight = 0b11111110
nine =  0b11110110
hex_a = 0b11101110
hex_b = 0b00111110
hex_c = 0b10011100
hex_d = 0b01111010
hex_e = 0b10011110
hex_f = 0b10001110
char_l = 0b00011100
char_ll = 0b01101100
char_left_one = 0b00001100
char_h = 0b01101110
char_o = 0b00111010

#this function will shift out to the 74HC595 shift register at about 500KHz clock
#of course, since we're using sleep_us(), we're not guaranteed to have EXACTLY this speed
#for our purposes, the 74HC595 most likely doesn't care, as long as we meet its
#generous timing requirements
def shift_out(sout):
    for i in range(0, 8):
        sr_clk.off()
        sr_data.value((sout >> i) & 0x1)
        sleep_us(1)
        sr_clk.on()
        sleep_us(1)
    #clock one more times to propagate value
    sr_clk.off()
    sleep_us(1)
    sr_clk.on()
    sleep_us(1)
    sr_clk.off()

#make sure our pins are all off before we start
sr_clk.off()
seg_digit3.off()
seg_digit2.off()
seg_digit1.off()
seg_digit0.off()
sr_data.off()
led_onboard.off()

#show signs of life even if the 7-segment/shift register is not hooked up right
led_onboard.on()
sleep_ms(500)
led_onboard.off()
sleep_ms(500)
led_onboard.on()
sleep_ms(500)
led_onboard.off()
print("7 segment should say \"HEllo.\" now!")

#demo: display "HEllo." on the 4-digit 7-segment display
#we are essentially rapidly flashing each character on
#each digit of the display, which takes advantage of
#human persistence of vision
while True:
    shift_out(char_h)
    seg_digit0.on()
    sleep_ms(4)
    seg_digit0.off()
    sleep_us(10)
    
    shift_out(hex_e)
    seg_digit1.on()
    sleep_ms(4)
    seg_digit1.off()
    sleep_us(10)
    
    shift_out(char_ll)
    seg_digit2.on()
    sleep_ms(4)
    seg_digit2.off()
    sleep_us(10)
    
    shift_out(char_o | dp)
    seg_digit3.on()
    sleep_ms(4)
    seg_digit3.off()
    sleep_us(10)
