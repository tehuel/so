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
    
    def interruptionStart(self):
        # interrupcion inicial, le doy un pcb al cpu
        logger.debug( "interruptionStart()" )
        self.cpu.setContext( self.scheduler.get() )

    def interruptionEnd(self):
        logger.debug( "interruptionEnd()" )
        self.changeContext()

    def interruptionIO(self):
        # TODO: write code...
        logger.debug( "interruptionIO()" )

    def interruptionTimeout(self):
        # TODO: write code...
        logger.debug( "interruptionTimeout()" )
        self.changeContext()

    def changeContext(self):
        # cambio de contexto. saco pcb de cpu y pongo siguiente pcb en cpu
        logger.debug( "changeContext()" )
        self.cpu.setContext( self.scheduler.get() )
        
