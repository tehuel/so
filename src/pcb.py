import logging

logger = logging.getLogger(__name__)

class PCB:
    # es creado por el kernel al ejecutar un programa

    def __init__( self, base, size, aPID ):
        logger.debug( "init" )
        self.pid = aPID
        self.base = base
        self.size = size
        self.state = "READY"
        self.pc = 0
        logger.debug( "PCB Created. PID %s. Base %s. Size: %s", self.pid, self.base, self.size )

    def updateState( self, newState ):
        logger.debug( "pcb.updateState())" )
        self.state = newState
        
    def getNext(self):
        #siguiente instruccion a ejecutar
        return self.base + self.pc
        
    def updatePC (self ):
        self.pc = self.pc + 1