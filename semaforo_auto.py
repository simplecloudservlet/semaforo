#!/bin/python
#SemaforoTel
#Author: Lucio A. Rocha
#Last update: 25/02/2022-12:02

import RPi.GPIO as GPIO
import sys
from time import sleep
from datetime import datetime

GPIO.setmode(GPIO.BCM)

#args = sys.argv
#mySleep = int(args[1]) #Receive mySleep as argument
mySleep = 10

R1 = 19
R2 = 26
R3 = 20
R4 = 21

#Initialize the ports
t = ( R1, R2, R3 )
c = ( 'VERMELHO', 'AMARELO', 'VERDE' )
for i in t:
   GPIO.setup(i, GPIO.OUT)
   GPIO.output(i,True) #disable port

try:
   while True:
      j=0
      for i in t:
        GPIO.output(i, False) #enable port
        print('[',str(datetime.now()),'] -> ',c[j],sep='')
        sleep(mySleep)
        GPIO.output(i, True) #disable port
        sleep(1)
        j=j+1
        if j>2: j=0
finally:
   GPIO.cleanup()
