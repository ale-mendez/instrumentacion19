#!/usr/bin/env python3
#
# execute as: sudo ./idn_instrument.py
#
import visa

rm=visa.ResourceManager('py')
device=[]
device=rm.list_resources()
print(device)
my_instrument=rm.open_resource(device[0])
whoami=my_instrument.query('*IDN?')
print('who am I?')
print(whoami)
