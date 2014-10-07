class MMU:
    # guarda todas las instrucciones de un programa, devolviendo posicion inicial
    # lee una instruccion en una posicion determinada

    def __init__(self, aMemory):
        self.memory = aMemory
        self.lastPosition = 0
        
    def loadProgram(self, aProgram):
        # agarra lista de instrucciones del programa y los guarda en memoria
        # devuelve posicion inicial en memoria
        self.initialPosition = self.lastPosition
        for instruction in aProgram.instructions:
            self.lastPosition = self.memory.write( instruction )
        return self.initialPosition

    def getInstruction(self, aCellNumber):
        # lee una posicion de memoria
        print("mmu: getInstruction", aCellNumber, self)
        self.foundInstruction = self.memory.read( aCellNumber )
        print("mmu: foundInstruction", self.foundInstruction)
        return ( self.foundInstruction )
