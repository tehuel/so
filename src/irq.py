import interruption
import logging

logger = logging.getLogger(__name__)

class IRQ:
    
    def __init__(self):
        self.cpu = None
        self.scheduler = None
        self.queue = []
    
    def setCPU(self, aCPU):
        self.cpu = aCPU
    
    def setScheduler(self, aScheduler):
        self.scheduler = aScheduler
        
    def raiseInterruption(self, anInterruption):
        logger.debug( "RAISE INTERRUPTION" )
        self.queue.insert( 0, anInterruption )
        
    def processInterruption(self):
        if ( self.queue ):
            self.queue.pop().run( self.scheduler, self.cpu )
