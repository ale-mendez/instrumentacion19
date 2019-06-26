from lantz.ino import INODriver, BoolFeat
from lantz.qt import Backend, Frontend, InstrumentSlot

class LEDDriver(INODriver):
    led = BoolFeat('LED')

if __name__ == '__main__':
    from lantz.core.log import log_to_screen, log_to_socket, DEBUG
    from lantz.qt import start_gui_app, wrap_driver_cls
    
    # ~ log_to_socket(DEBUG) # Uncommment this line to log to socket
    log_to_screen(DEBUG) # or comment this line to stop logging

    with LEDDriver.via_packfile('LEDDriver.pack.yaml', check_update=True) as board:
        board.led = True
        board.led = False
        print(board.led)
