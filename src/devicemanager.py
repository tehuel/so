from disk import *
from mmu import *
from memory import *
from clock import *
from cpu import *
from iodevice import *

import logging

class DeviceManager:
# crea y maneja todos los dispositivos

    def __init__(self):
        # inicializacion de todos los dispositivos
        logging.debug( "devicemanager.init" )
        self.mem = Memory()
        self.mmu = MMU( self.mem )
        self.disk = Disk()
        self.cpu = CPU()
        self.clock = Clock(self.cpu)
        #io devices