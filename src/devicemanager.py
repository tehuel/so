from clock import *
from disk import *
from memory import *
from mmu import *
from cpu import *
from iodevice import *

import logging

logger = logging.getLogger(__name__)

class DeviceManager:
# crea y maneja todos los dispositivos

    def __init__(self):
        # inicializacion de todos los dispositivos
        logger.debug( "init" )
        self.disk = Disk()
        self.memory = Memory()
        self.mmu = MMU( self.memory )
        self.cpu = CPU( self.mmu )
        self.clock = Clock( self.cpu )
        #io devices