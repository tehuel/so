class PCB:
    # es creado por el kernel al ejecutar un programa

    def __init__( self, memoryPos, aPID ):
        self.pid = aPID
        self.state = "READY"
        self.memoryPos = memoryPos
        self.pc = 0
