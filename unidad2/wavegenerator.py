#!/usr/bin/env python3
#
import visa

rm=visa.ResourceManager('py')
device=[]
device=rm.list_resources()

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
my_instrument.freq_fix('100Hz')
# set voltaje amplitude
my_instrument.voltaje(2.5,'VPP')
# set voltaje offset
my_instrument.volt_offset(0,'mV')
