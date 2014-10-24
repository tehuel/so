import logging

logger = logging.getLogger(__name__)

class Memory:
    # guarda una lista de instrucciones

    def __init__(self):
        self.memoryCells = []

    def read(self, aCellNumber):
        logger.debug("read [%s]: %s", aCellNumber, self.memoryCells[ aCellNumber ].text)
        return self.memoryCells[ aCellNumber ]

    def write(self, aCellNumber, anInstruction):
        self.memoryCells.insert(aCellNumber, anInstruction)
        logger.debug("written [%s]: %s", aCellNumber, anInstruction.text)
