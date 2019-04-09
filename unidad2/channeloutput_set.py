#!/usr/bin/env python3
#
# execute as: sudo ./read_instrument.py
#

import visa

rm=visa.ResourceManager('py')
device=[]
device=rm.list_resources()
my_instrument=rm.open_resource(device[0])

# query state of channel 1 (ON/OFF)
output=my_instrument.query('OUTPut1:STATe?')
print(output.strip())

# if on => off
if output.strip() == str(1):
    print('apagando channel 1')
    my_instrument.write('OUTPut1:STATe OFF',0)

# if off => on
if output.strip() == str(0 ):
    print('encendiendo channel 1')
    my_instrument.write('OUTPut1:STATe ON')
