#!/usr/bin/env python3
from gpiozero import LED
from time import sleep

from tkinter import *
from tkinter import Tk,Frame,BOTH


#w1= pause time before intervals start
#w2= number of reps
#w3= time between reps


print ('This is optozero running as newacg7.py. Starting program')

tup=1.3
tdown=1.46

def splash():
    timex=Tk()
    timex.geometry('800x480+0+40')
    w=Label(timex, text='Pull on the Budgie Smugglers', font='Verdana 30 bold')
    
    w.pack()
    w=Label(timex, text='Starting Program', font='Verdana 30 bold',fg='red')
    
    w.pack()

    
    w.after(3000, lambda: timex.destroy())
    timex.mainloop()

def mainnorm():
    
    led12 = LED(12)
    led24 = LED(24)
    m=w2.get()
    n=0
    p=w3.get()
    
    delay=w1.get()
    delay=delay*60
    master.destroy()
    splash()
    
    print ('Intro for',(delay/60),'minutes',' ,Diff=Norm', 'No. Intervals=',m,)
    sleep(delay)

    while n<m:
        
        global tup
        led24.on()
        sleep(tup)
        print ('Paused by ',p,'Increasing by',(tup),)
        led24.off()
        sleep(p)
        led12.on()
        print ('Paused by ',p,'Decreasing by',(tdown))
        sleep(tdown)
        led12.off()
        sleep(p)
        n=n+1
        if n==1:
            tup=1.45
        
        if n==2:
            tup=1.49
         
        if n==3:
            tup=1.50
         
        if n==4:
            tup=1.51
         

        
    input ('waitingabit')
    exit()

def maineasy():

    led12 = LED(12)
    led24 = LED(24)
    m=w2.get()
    n=0
    p=w3.get()
    
    delay=w1.get()
    delay=delay*60
    master.destroy()
    splash()
    
    print ('Intro for',(delay/60),'minutes',' ,Diff=Easy', 'No. Intervals=',m,)
    sleep(delay)
    global tup,tdown
    tup=0.9
    tdown=0.925
        

    while n<m:
        
        led24.on()
        sleep(tup)
        print ('Paused by ',p,'Increasing by',(tup),)
        led24.off()
        sleep(p)
        led12.on()
        print ('Paused by ',p,'Decreasing by',(tdown))
        sleep(tdown)
        led12.off()
        sleep(p)
        n=n+1
        if n==1:
            tup=0.9
        
        if n==2:
            tup=1
         
        if n==3:
            tup=1.1
         
        if n==4:
            tup=1.1
         

        
    input ('waitingabit')
    exit()

def mainslider():
    global w2,w1,w3,master
    master = Tk()
    master.geometry('800x480+0+40')
    w1 = Scale(master, from_=10, to=30, length=400,tickinterval=2, orient=HORIZONTAL,bd=5,highlightbackground='black',label='Length of Introduction, (minutes)') 
    w1.set(20)
    w1.pack()
    w2 = Scale(master, from_=0, to=10, length=400,tickinterval=1, orient=HORIZONTAL,bd=5,highlightbackground='black',label='Number of Intervals') 
    w2.set(5)
    w2.pack()
    w3 = Scale(master, from_=60, to=120, length=400,tickinterval=5, orient=HORIZONTAL,bd=5,highlightbackground='black',label='Length of Intervals, (seconds)') 
    w3.set(90)
    w3.pack()
    
    Button(master, text='Easy', command=maineasy).pack(padx=10,pady=10)
    Button(master, text='Norm', command=mainnorm).pack(padx=0,pady=10)

    mainloop()

mainslider()
