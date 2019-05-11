#!/usr/bin/env python3

import visa
#from matplotlib import pyplot as plt
import numpy as np
import os, sys
import csv

rm=visa.ResourceManager('py')
device=[]
device=rm.list_resources()

print(device)

class Osciloscopio:
	
	def __init__(self, devnumber):
		self.devnumber = devnumber
		self.oscilo = rm.open_resource(devnumber)
	
	def quien_soy(self):
		return self.oscilo.query('*IDN?')
		
	def auto_set(self):
		self.oscilo.write('AUTOSet')
		
	def header_state(self):
		return self.oscilo.query('HEADer?')
	
	def header_off(self):
		self.oscilo.write('HEADer OFF')	
	
	def trigger_cuanto_es(self):
		return self.oscilo.query('TRIGger?')
	
	def trigger_set(self, voltaje_trigger):
		self.oscilo.write('TRIGger:MAIn:LEVel'+str(voltaje_trigger))
	
	def trigger_pulso(self, channel):
		self.oscilo.write('TRIGger:MAIn:PULse:SOUrce '+str(channel)) 
		
	def tiempo_que_usas(self):
		return self.oscilo.query('HORizontal:DELay?')
		
	def tiempo_set(self, tiempo):
		self.oscilo.write('HORizontal:MAIn:SCAle '+str(tiempo))
	
	def voltaje_ch1(self, channel, voltaje):
		self.oscilo.write('CH'+str(channel)+':SCAle '+str(voltaje))
		
	def set_del_ch1(self, channel):
		return self.oscilo.query('CH'+str(channel)+'?')	
	
	def pantalla(self):
		xze, xin, yze, ymu, yoff = self.oscilo.query_ascii_values('WFMPRE:XZE?;XIN?;YZE?;YMU?;YOFF?;', 	separator=';')
		self.oscilo.write('DATa:SOUrce CH1')
		self.oscilo.write('DAT:ENC RPB')
		self.oscilo.write('DAT:WID 1')
		data = self.oscilo.query_binary_values('CURV?', datatype='B', container=np.array)
		tiempo = xze + np.arange(len(data)) * xin
#            print(tiempo,data)
#		plt.plot(tiempo, data);
#		plt.xlabel('Tiempo [s]');
#		plt.ylabel('Voltaje [V]');
#		plt.show()
#            return data, tiempo


Oscilo=Osciloscopio(device[0])
Channel=1
Volt_set=1
voltaje_trigger=0.5
tiempo=5E-2

print(Oscilo.quien_soy())
Oscilo.tiempo_set(tiempo)
print(Oscilo.tiempo_que_usas())
print(Oscilo.set_del_ch1(Channel))
Oscilo.voltaje_ch1(Channel,Volt_set)
print(Oscilo.trigger_cuanto_es())
Oscilo.header_off()
Oscilo.pantalla()
#data, tiempo = Oscilo.pantalla()

print(data)
print(tiempo)





