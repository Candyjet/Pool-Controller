#!/usr/bin/env python3
from gpiozero import LED
from time import sleep
import time
print ('This is Opto Zero')

led12 = LED(12)
led24 = LED(24)


tup=1.3
tdown=1.46

def speeddown():
    print("Decreasing by",'%2f'%tdown)
    
    led12.on()
    time.sleep(tdown)
    led12.off()
    


def speedup():
    print("Increasing by",'%2f'%tup)
    
    led24.on()
    time.sleep(tup)
    led24.off()
    

pauset=2
n=0
print ('Starting Sequence')

time.sleep(2)
while n<2:
    speedup()   
    time.sleep(pauset)
    speeddown()
    time.sleep(pauset)
    n=n+1
   
    if n==1:
        tup=1.45
        
    if n==2:
         tup=1.47
         
    if n==3:
         tup=1.50
         
    if n==4:
         tup=1.51
         

    
#GPIO.cleanup()



