class Program:
    # es una lista de instrucciones, con un nombre

    def __init__(self, aName):
        self.name = aName
        self.instructions = []

    def addInstruction(self, anInstruction):
        self.instructions.append(anInstruction)

    def execute(self, console):
        for inst in self.instructions:
            inst.execute(console)
