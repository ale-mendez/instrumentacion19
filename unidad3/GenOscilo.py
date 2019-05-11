#!/usr/bin/env python3
#
import visa
#from matplotlib import pyplot as plt
import numpy as np
import os, sys
import time

# GENERADOR

rm=visa.ResourceManager('py')
device=[]
device=rm.list_resources()

#print(device)

#sys.exit()

class Instrumento:

    def __init__(self, serialno):
        self.serial = serialno
        self.instr = rm.open_resource(serialno)


class WaveGenerator(Instrumento):

    ##@Feat()
    def who_am_i(self):
        idn = self.instr.query('*IDN?')
        return idn.strip()

    def which_freq_mod(self):
        mod = self.instr.query('SOURce1:FREQuency:MODE?')
        return mod.strip()

    # def which_volt_amp(self):
    #     dum = self.instr.query('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude?')
    #     return float(dum)
    #
    # def which_volt_min(self):
    #     dum = self.instr.query('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude? MINimum')
    #     return float(dum)
    #
    # def which_volt_max(self):
    #     dum = self.instr.query('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude? MAXimum')
    #     return float(dum)
    #
    # def which_volt_unit(self):
    #     return self.instr.query('SOURce1:VOLTage:UNIT?')

    def which_volt_amp(self):
        amp = self.instr.query('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude?')
        ampmin = self.instr.query('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude? MINimum')
        ampmax = self.instr.query('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude? MAXimum')
        ampunit = self.instr.query('SOURce1:VOLTage:UNIT?')
        return float(amp), float(ampmin), float(ampmax), ampunit.strip()

    def which_volt_offset(self):
        voff = self.instr.query('SOURce1:VOLTage:OFFSet?')
        voffmin = self.instr.query('SOURce1:VOLTage:OFFSet? MINimum')
        voffmax = self.instr.query('SOURce1:VOLTage:OFFSet? MAXimum')
        return float(voff), float(voffmin), float(voffmax)

    def freq_mod(self, modtype):
        # options:
        # CW|SWEep
        print('Setting new freq mode:')
        if modtype == 'CW':
            print(' ==> CW (continuous wave)')
        if modtype == 'SWEep':
            print(' ==> Sweep')
        return self.instr.write('SOURce1:FREQuency:MODE {}'.format(modtype))

    def freq_fix(self,freq):
        return self.instr.write('SOURce1:FREQuency:FIXed {}'.format(freq))

    def func_shape(self,ishape):
        # options:
        # SINusoid|SQUare|PULSe|RAMP|PRNoise|DC|SINC|GAUSsian|LORentz|ERISe|EDECay|HAVersine
        print('Setting new function: \n ==> {} function'.format(ishape))
        return self.instr.write('SOURce1:FUNCtion:SHAPe {}'.format(ishape))

    def voltaje(self,amplitude,units):
        # options:
        # VPP|VRMS|DBM
        if amplitude > voltmax:
            raise ValueError(' *** input amplitude should be smaller than {} *** '.format(voltmax))
        if amplitude < voltmin:
            raise ValueError(' *** input amplitude should be greater than {} *** '.format(voltmin))
        newvolt=str(amplitude)+" "+units
        print('Setting new voltaje: \n ==> {} {}'.format(amplitude,units))
        return self.instr.write('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude {} {}'.format(amplitude,units))

    def volt_offset(self,voffset,units):
        print('Setting new offset voltaje: \n ==> {} {}'.format(voffset,units))
        return self.instr.write('SOURce1:VOLTage:LEVel:IMMediate:OFFSet {} {}'.format(voffset,units))

# define instrument
my_instrument = WaveGenerator(device[0])

whoami = my_instrument.who_am_i()
deffreqmod = my_instrument.which_freq_mod()
# whichvoltamp = my_instrument.which_volt_amp()
# whichvoltunit = my_instrument.which_volt_unit()
# voltmin = my_instrument.which_volt_min()
# voltmax = my_instrument.which_volt_max()
defvoltamp, defvoltmin, defvoltmax, defvoltunit = my_instrument.which_volt_amp()
voltmin = float(defvoltmin)
voltmax = float(defvoltmax)
defvoffset, defvoffmin, defvoffmax = my_instrument.which_volt_offset()

print('Current instrument:',whoami)
print('DEFAULT VALUES:')
print('---------------')
print(' Frequency mode:',deffreqmod)
print(' Voltaje:',defvoltamp,defvoltunit)
print('     min:',voltmin,defvoltunit)
print('     max:',voltmax,defvoltunit)
print(' Offset:',defvoffset)

print('\nNEW VALUES:')
print('-------------')
# set frequency mode:
my_instrument.freq_mod('CW')
# set function shape
my_instrument.func_shape('SIN')
# set fixed frequency value
my_instrument.freq_fix('1MHz')
# set voltaje amplitude
my_instrument.voltaje(1,'VPP')
# set voltaje offset
my_instrument.volt_offset(0,'mV')

#sys.exit()

# OSCILOSCOPIO

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
	
	def voltaje_ch(self, channel, voltaje):
		self.oscilo.write('CH'+str(channel)+':SCAle '+str(voltaje))
		
	def set_del_ch(self, channel):
		return self.oscilo.query('CH'+str(channel)+'?')	
	
	def pantalla(self, channel):
		xze, xin, yze, ymu, yoff = self.oscilo.query_ascii_values('WFMPRE:XZE?;XIN?;YZE?;YMU?;YOFF?;', 	separator=';')
		self.oscilo.write('DATa:SOUrce CH'+str(channel))
		self.oscilo.write('DAT:ENC RPB')
		self.oscilo.write('DAT:WID 1')
		data = self.oscilo.query_binary_values('CURV?', datatype='B', container=np.array)
		tiempo = xze + np.arange(len(data)) * xin
#		plt.plot(tiempo, data);
#		plt.xlabel('Tiempo [s]');
#		plt.ylabel('Voltaje [V]');
#		plt.show()


Oscilo=Osciloscopio(device[1])
Channel=2
Volt_set=1
voltaje_trigger=0.5
tiempo=5E-2

print(Oscilo.quien_soy())
Oscilo.tiempo_set(tiempo)
print(Oscilo.tiempo_que_usas())
print(Oscilo.set_del_ch(Channel))
Oscilo.voltaje_ch(Channel,Volt_set)
print(Oscilo.trigger_cuanto_es())
Oscilo.pantalla(Channel)


sys.exit()

# Intento un ciclo facil

x=[0.2 , 0.3 , 0.4 , 0.5]

for i in range(5):
	my_instrument.voltaje(x[i],'VPP')
	time.sleep(.5)
	

# Guardar los datos en un archivo .dat

text_file = open("Output.txt", "w")

text_file.write("Hello")

text_file.close()
