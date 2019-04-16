#!/usr/bin/env python3
#


import visa
from lantz.messagebased import MessageBasedDriver


rm=visa.ResourceManager('py')
device=[]
device=rm.list_resources()


class WaveGenerator(MessageBasedDriver):

    ##@Feat()
    def who_am_i(self):
        idn = self.query('*IDN?')
        return idn.strip()


# define instrument
my_instrument = WaveGenerator(device[0])

whoami = my_instrument.who_am_i()
