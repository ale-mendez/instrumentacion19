# notas de clase (incompleto)

from lantz import Feat
from lantz.messagebased import MessageBasedDriver

class Osci1(MessageBasedDriver):

    @Feat()
    def idn(self):
        return self.query('*IDN?')


class Osci2(MessageBasedDriver):
    @Feat()
    def idn(self):
        return self.query('*IDN?')

    @Feat(units='s')
    def timebase(self):
        return  self.write('HOR:MAIN:SCA?')

    @timebase.setter
    def timebase(self,value):
        return self.write('HOR:MAIN:SCA {}'.format(value))

class Osci3(MessageBasedDriver):

    @Feat()
    def idn(self):
        return self.query('*IDN?')

    set_query =
