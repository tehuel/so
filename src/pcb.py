import logging

class PCB:
    # es creado por el kernel al ejecutar un programa

    def __init__( self, base, size, aPID ):
        logging.debug( "pcb.init" )
        self.pid = aPID
        self.base = base
        self.size = size
        self.state = "READY"
        self.pc = 0

    def updateState( self, newState ):
        logging.debug( "pcb.updateState())" )
        self.state = newState
        
    def getPC (self):
        logging.debug( "pcb.getPC()" )
        return self.pc
        
    def getNext(self):
        logging.debug( "pcb.getNext()" )
        return self.base + self.pc
        
    def getPID(self):
        logging.debug( "pcb.getPID()" )
        return self.pid
        
    def updatePC (self, newPC ):
        logging.debug( "pcb.updatePC()" )
        self.pc = newPC