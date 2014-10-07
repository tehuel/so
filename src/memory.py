class Memory:
    # guarda una lista de instrucciones

    def __init__(self):
        self.memoryCells = []

    def read(self, aCellNumber):
        return self.memoryCells[ aCellNumber ]

    def write(self, anInstruction):
        self.memoryCells.append ( anInstruction )
