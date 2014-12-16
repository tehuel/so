import logging

logger = logging.getLogger(__name__)

class Memory:
    # guarda una lista de instrucciones

    def __init__(self, memorySize):
        self.cells = {}
        self.size = memorySize
        
        # inicializo (None) todas las celdas de memoria
        cell = 0
        while ( cell <= self.size ):
            self.cells[cell] = None
            cell += 1 

    def __repr__(self):
        return "{0} Cells\n{1}".format(self.size, self.cells)

    def read(self, aCellNumber):
        logger.debug("read [%s]: %s", aCellNumber, self.cells[ aCellNumber ])
        return self.cells[ aCellNumber ]

    def write(self, aCellNumber, anInstruction):
        self.cells[aCellNumber] = anInstruction
        logger.debug("written [%s]: %s", aCellNumber, anInstruction)
