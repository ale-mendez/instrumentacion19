#!/usr/bin/env python3

import visa

rm=visa.ResourceManager()
# print the USB id of the instrument
print(rm.list_resources())
# open the instrument with a specific id
my_instrument=rm.open_resource('USB0::1689::838::C033248::0::INSTR')
# query the device with '\*IDN?', which stands for “what are you?” 
# or “what’s on your display at the moment?”. 
print(my_instrument.query('*IDN?'))
# we can also ask like
my_instrument.write('*IDN?')
print(my_instrument.read())

