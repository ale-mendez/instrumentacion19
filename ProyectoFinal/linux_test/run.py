from lantz.ino import INODriver, BoolFeat, QuantityFeat
from lantz.qt import Backend, Frontend, InstrumentSlot

class MiDriver(INODriver):
    motor = QuantityFeat('MOTOR', getter=False)
    pow_diodo = QuantityFeat('DIODO', setter=False)
    pow_laser = QuantityFeat('LASER', getter=False)


if __name__ == '__main__':
    from lantz.core.log import log_to_screen, log_to_socket, DEBUG
    from lantz.qt import start_gui_app, wrap_driver_cls
    
    # ~ log_to_socket(DEBUG) # Uncommment this line to log to socket
    log_to_screen(DEBUG) # or comment this line to stop logging

    QMiDriver = wrap_driver_cls(MiDriver)
    with QMiDriver.via_packfile('MiDriver.pack.yaml', check_update=True) as board:
#        board.motor = 0
         board.pow_laser = 10
        #print(angulo.potencia)
