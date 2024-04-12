#!/bin/python
#SemaforoTel: server
#Author: Lucio A. Rocha
#Last update: 25/02/2022-17:24

import web
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import sys
from os.path import exists
from os import remove

mySleep = 10

R1 = 19
R2 = 26
R3 = 20
R4 = 21

#Enable auto
cookie = "/home/pi/cookie.txt"

#Initialize the ports
t = ( R1, R2, R3 )
c = ( 'VERMELHO', 'AMARELO', 'VERDE' )

GPIO.setmode(GPIO.BCM)

for i in t:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i,True) #disable port

render = web.template.render('/home/pi/templates/')
urls = (
	'/','index',
	'/update','update',
	'/auto','auto'
)

class index:
	def GET(self):
		GPIO.output(R1, True) 		
		GPIO.output(R2, True) 		
		GPIO.output(R3, True) 		
		
		if exists(cookie):
			remove(cookie)

		return render.index('')
class update:
	def GET(self):
		campo = int(web.input(led=0).led)
		if campo==1:
			GPIO.output(R1, False) #enable
			GPIO.output(R2, True) 
			GPIO.output(R3, True) 
		elif campo==2:
			GPIO.output(R1, True) 		
			GPIO.output(R2, False) #enable
			GPIO.output(R3, True)
		elif campo==3:
			GPIO.output(R1, True) 		
			GPIO.output(R2, True) 
			GPIO.output(R3, False) #enable
		else:
			GPIO.output(R1, True) 		
			GPIO.output(R2, True) 
			GPIO.output(R3, True) 

		if exists(cookie):
			remove(cookie)	
		return render.index(campo)

class auto:
	def GET(self):
		try:
			f = open(cookie,"w")
			f.close()

			while exists(cookie):
				j=0
				for k in t:

					#disable all
					for i in t:
						GPIO.output(i, True) #disable
					
					GPIO.output(k, False) #enable port
					print('[',str(datetime.now()),'] -> ',c[j],sep='')
					sleep(mySleep)
					GPIO.output(k, True) #disable port
					sleep(1)
					j=j+1
					if j>2: j=0
		except Exception as e:
			print('Error:',str(e))

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
