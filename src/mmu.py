import logging

logger = logging.getLogger(__name__)

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
        
        logger.info( "Load program %s ", aProgram.name )
        
        for instruction in aProgram.instructions:
            logger.debug( "write to memory( %s )", self.lastPosition)
            self.memory.write( self.lastPosition, instruction )
            self.lastPosition += 1
        return self.initialPosition

    def getInstruction(self, aCellNumber):
        # lee una posicion de memoria
        self.foundInstruction = self.memory.read( aCellNumber )
        return ( self.foundInstruction )
