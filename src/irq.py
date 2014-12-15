import interruption
import logging

logger = logging.getLogger(__name__)

class IRQ:
    
    def __init__(self):
        self.cpu = None
        self.scheduler = None
        self.queue = []
    
    def setScheduler(self, aScheduler):
        self.scheduler = aScheduler
        
    def setCPU(self, aCPU):
        self.cpu = aCPU
        self.cpu.quantum = self.scheduler.quantum
        logger.debug("Quantum set on CPU from Scheduler")
    
    def raiseInterruption(self, anInterruption):
        self.queue.insert( 0, anInterruption )
        logger.debug( "New Interruption Raised" )
        
    def processInterruption(self):
        if ( self.queue ):
            self.queue.pop().run( self.scheduler, self.cpu )
