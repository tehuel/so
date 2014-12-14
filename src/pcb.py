import logging

logger = logging.getLogger(__name__)

class PCB:
    # es creado por el kernel al ejecutar un programa

    def __init__( self, name, base, size, aPID, aPriority=None ):
        self.name = name
        self.base = base
        self.size = size
        self.pid = aPID
        self.state = "READY"
        self.pc = 0
        self.priority = aPriority
        logger.debug( str(self) )

    def __str__(self):
        if (self.priority):
            return "PID: {0}. Priority: {1}. Name: {2}. Base: {3}. Size: {4}".format(self.pid, self.priority, self.name, self.base, self.size)
        else:
            return "PID: {0}. Name: {1}. Base: {2}. Size: {3}".format(self.pid, self.name, self.base, self.size)
        
    def updateState( self, newState ):
        logger.debug( "pcb.updateState())" )
        self.state = newState
        
    def getNextInstruction(self):
        #siguiente instruccion a ejecutar
        return self.base + self.pc
        
    def updatePC (self ):
        self.pc = self.pc + 1