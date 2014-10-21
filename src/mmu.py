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
        logger.debug( "Initial Position( %s )", self.initialPosition )
        
        for instruction in aProgram.instructions:
            self.lastPosition = self.memory.write( instruction )
            logger.debug( "Memory Written( %s: \'%s\' )", self.lastPosition, instruction.text )
        return self.initialPosition

    def getInstruction(self, aCellNumber):
        # lee una posicion de memoria
        self.foundInstruction = self.memory.read( aCellNumber )
        logger.debug( "FoundInstruction( %s: \'%s\' )", aCellNumber, self.foundInstruction.text )
        return ( self.foundInstruction )
