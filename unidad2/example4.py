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

    def who_am_i(self):
        return self.instr.query('*IDN?')

class WaveGenerator(Instrumento):

    def which_freq_mod(self):
        return self.instr.query('SOURce1:FREQuency:MODE?')

    def freq_mod(self, modtype):
        # options:
        # CW|SWEep
        if modtype == 'CW':
            print('setting freq mode == CW (continuous wave)')
        if modtype == 'SWEep':
            print('setting freq mode == sweep')
        return self.instr.write('SOURce1:FREQuency:MODE '+modtype)

    def freq_fix(self,freq):
        return self.instr.write('SOURce1:FREQuency:FIXed '+freq)

    def func_shape(self,ishape):
        # options:
        # SINusoid|SQUare|PULSe|RAMP|PRNoise|DC|SINC|GAUSsian|LORentz|ERISe|EDECay|HAVersine
        print('setting '+ishape+' function')
        return self.instr.write('SOURce1:FUNCtion:SHAPe '+ishape)
    # def set_timebase(self, seconds):
        # 'HOR:DEL:SCA {}'.format(seconds)
        # hacer algo

my_instrument = WaveGenerator(device[0])

whoami = my_instrument.who_am_i()
print('My current instrument is: \n',whoami.strip())

whichfreqmod = my_instrument.which_freq_mod()
print(whichfreqmod.strip())
# set frequency mode:
my_instrument.freq_mod('CW')
# set function shape
my_instrument.func_shape('SQU')
# set fixed frequency value
my_instrument.freq_fix('500kHz')
