#!/usr/bin/env python3

import visa

rm=visa.ResourceManager()
# print the USB id of the instrument
print(rm.list_resources())
# open the instrument with a specific id
my_instrument=rm.open_resource('USB0::1689::838::C033248::0::INSTR')

# para una osciloscopio:
# read data raw
my_instrument.read_raw() # in binary ==> #<x><yyyy>
my_instrument.write('DATa:ENCdg ASCII') # changed to ascii
my_instrument.write('CURVE?')
my_instrument.read()
x=my_instrument.query_ascii_values('CURVE?') # define values in list
