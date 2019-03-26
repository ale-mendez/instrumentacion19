#!/usr/bin/env python3

import visa

rm=visa.ResourceManager()
# print the USB id of the instrument
print(rm.list_resources())
# open the instrument with a specific id
my_instrument=rm.open_resource('USB0::1689::838::C033248::0::INSTR')

# NO FUNCA
my_instrument.write('SOURce1:FM:INTernal:FREQuency 10kHz')

