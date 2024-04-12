#!/bin/python
# SemaforoTel
# Description: Stop semaforo running
# Author: Lucio A. Rocha
# Last update: 25/02/2022 - 13:16

import os, subprocess

#r = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE)
#print(r.stdout,'.')

# Try to kill 'semaforo_auto.py'
pid = subprocess.check_output('ps aux | grep semaforo_auto | head -n 1 | awk \'{print $2}\'', shell=True, text=True)
print('+SemaforoTel PID:',pid)

try:
	cmd = 'kill -9 ' + pid
	s = subprocess.check_output(cmd, shell=True, text=True)
	print(s)
except:
	print('No semaforo_auto.py active.')


# Try to kill 'servidor.py'
pid = subprocess.check_output('ps aux | grep servidor.py | head -n 1 | awk \'{print $2}\'', shell=True, text=True)
print('+Servidor PID:',pid)

try:
	cmd = 'kill -9 ' + pid
	s = subprocess.check_output(cmd, shell=True, text=True)
	print(s)
except:
	print('No servidor.py active.')

#Clean GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

R1 = 19
R2 = 26
R3 = 20
R4 = 21

#Initialize the ports
t = ( R1, R2, R3 )

for i in t:
   GPIO.setup(i, GPIO.OUT)
   GPIO.output(i,True) #disable port

GPIO.cleanup()
