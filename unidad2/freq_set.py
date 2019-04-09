#!/usr/bin/env python3
#
# execute as: sudo ./read_instrument.py
#
import visa

rm=visa.ResourceManager('py')
device=[]
device=rm.list_resources()
my_instrument=rm.open_resource(device[0])

# query frequency mode of channel 1
freqmod=my_instrument.query('SOURce1:FREQuency:MODE?')
# print(freqmod)
# set frequency mode of channel 1
print('setting freq mode == continuous')
freqmode=my_instrument.write('SOURce1:FREQuency:MODE CW')
# set frequency to particular value
print('setting freq value == 1kHz')
freqsetval=my_instrument.write('SOURce1:FREQuency:CW 1kHz')
