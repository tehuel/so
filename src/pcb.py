class PCB:
    # es creado por el kernel al ejecutar un programa

    def __init__( self, base, size, aPID ):
        self.pid = aPID
        self.base = base
        self.size = size
        self.state = "READY"
        self.pc = 0
        print("pcb created", self.pid)

    def updateState( self, newState ):
        self.state = newState
        
    def getPC (self):
        return self.pc
        
    def getNext(self):
        return self.base + self.pc
        
    def getPID(self):
        return self.pid
        
    def updatePC (self, newPC ):
        self.pc = newPC