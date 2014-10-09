import logging
import pcb

class Kernel:

    def __init__(self, aDeviceManager, aIRQ, aScheduler, aConsole):
        self.lastPID = 0
        self.devicemanager = aDeviceManager
        self.irq = aIRQ
        self.scheduler = aScheduler
        self.console = aConsole
        
        #initialize
        logging.debug( "kernel.init" )
        self.devicemanager.cpu.setIRQ(self.irq)
        self.irq.setCPU(self.devicemanager.cpu)
        self.irq.setScheduler(self.scheduler)
        
    def generatePID(self):
        self.lastPID += 1
        logging.debug( "kernel.generatePID()" )
        return self.lastPID

    def execute(self, aProgramName):
        #obtengo el programa del disco, lo paso a memoria, y creo el pcb correspondiente
        
        logging.debug( "kernel.execute()" )
        program = self.devicemanager.disk.getProgram( aProgramName )
        base = self.devicemanager.mmu.loadProgram( program )
        size = len(program.instructions)
        aPCB = pcb.PCB(base, size, self.generatePID() )
        
        #agrego el pcb a la lista de pcbs
        self.scheduler.add( aPCB )
        