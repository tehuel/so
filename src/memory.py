import logging

logger = logging.getLogger(__name__)

class Memory:
    # guarda una lista de instrucciones

    def __init__(self, memorySize):
        memoryCells = {}
        cell = 0
        # inicializo todas las celdas de memoria
        while ( cell <= memorySize ):
            memoryCells[cell] = None
            cell += 1 
        self.memoryCells = memoryCells

    def read(self, aCellNumber):
        logger.debug("read [%s]: %s", aCellNumber, self.memoryCells[ aCellNumber ])
        return self.memoryCells[ aCellNumber ]

    def write(self, aCellNumber, anInstruction):
        self.memoryCells[aCellNumber] = anInstruction
        logger.debug("written [%s]: %s", aCellNumber, anInstruction)
