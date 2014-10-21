class Instruction:

    def __init__(self, aText, isIOInstruction = False):
        self.text = aText
        self.io = isIOInstruction

    def execute(self, aConsole):
        self.console = aConsole
        self.console.out(self.text)
        
    def isIO( self ):
        return self.io
