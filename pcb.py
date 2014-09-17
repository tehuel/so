class PCB:
    # es creado por el kernel al ejecutar un programa

    def __init__( self, memoryPos, aPID ):
        self.pc = 0
        self.memoryPos = memoryPos
        self.state = "READY"
        self.pid = aPID
