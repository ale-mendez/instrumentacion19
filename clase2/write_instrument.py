#!/usr/bin/env python3
#
# execute as: sudo ./write_instrument.py
#
import visa

rm=visa.ResourceManager()

# print the USB id of the instrument
device=[]
device=rm.list_resources()

# open the instrument with a specific id
my_instrument=rm.open_resource(device[0])
print(my_instrument)

# reset values
my_instrument.write('*RST')

# NO FUNCA
#my_instrument.write('SOURce1:AM:INTernal:FREQuency 10kHz')

