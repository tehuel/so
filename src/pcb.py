class PCB:
    # es creado por el kernel al ejecutar un programa

    def __init__( self, base, aPID ):
        self.pid = aPID
        self.base = base
        self.state = "READY"
        self.pc = 0

    def updateState( self, newState ):
        self.state = newState
        
    def updatePC (self, newPC ):
        self.pc = newPC