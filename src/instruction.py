class Instruction:

    def __init__(self, aText, isIOInstruction = False):
        self.text = str(aText)
        self.io = isIOInstruction
        
    def __repr__(self):
        if ( self.isIO() ):
            return self.text + "<IO>"
        else:
            return self.text + "<CPU>"

    def execute(self, aConsole):
        self.console = aConsole
        self.console.out(self.text)
        
    def isIO( self ):
        return self.io
