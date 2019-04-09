#!/usr/bin/env python3
#
# execute as: sudo ./reset_instrument.py
#
import visa

rm=visa.ResourceManager('py')
device=[]
device=rm.list_resources()
my_instrument=rm.open_resource(device[0])

# reset values
print('reset instrument...')
my_instrument.write('*RST')
