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
        logger.debug( "PCB Created. " + str(self) )

    def __repr__(self):
        string = "PCB(pid:{0} name:{1} pc:{4})".format(self.pid, self.name, self.base, self.size, self.pc)
        if (self.priority):
            string = string + " Priority: {0}.".format(self.priority)
            
        return string
        
    def updateState( self, newState ):
        logger.debug( "pcb.updateState())" )
        self.state = newState
        
    def getNextInstruction(self):
        #siguiente instruccion a ejecutar
        return self.base + self.pc
        
    def updatePC (self ):
        self.pc = self.pc + 1