from irq import *
from scheduler import *
import pcb

import logging

logger = logging.getLogger(__name__)


class Kernel:

    def __init__(self, aDeviceManager):
        self.lastPID = 0
        self.devicemanager = aDeviceManager

        self.irq = IRQ()
        self.scheduler = Scheduler()

        #initialize
        self.devicemanager.cpu.setIRQ(self.irq)
        self.irq.setScheduler(self.scheduler)
        self.irq.setCPU(self.devicemanager.cpu)
        
    def generatePID(self):
        self.lastPID += 1
        logger.debug( "generatePID( %s )", self.lastPID )
        return self.lastPID

    def execute(self, aProgramName):
        #obtengo el programa del disco, lo paso a memoria, y creo el pcb correspondiente
        
        logger.debug( "execute( %s )", aProgramName )
        program = self.devicemanager.disk.getProgram( aProgramName )
        base = self.devicemanager.mmu.loadProgram( program )
        size = len(program.instructions)
        aPCB = pcb.PCB(program.name, base, size, self.generatePID() )
        
        #agrego el pcb a la lista de pcbs
        self.scheduler.add( aPCB )
        