import pcb

class Kernel:
    # crea procesos
    lastPID = 0

    def __init__(self, aConsole, aDisk, aMemoryManager):
        self.console = aConsole
        self.disk = aDisk
        self.mm = aMemoryManager
        
    def generatePID(self):
        self.lastPID += 1
        return self.lastPID

    def execute(self, aProgramName):
        #obtengo el programa del disco, lo paso a memoria, y creo el pcb correspondiente
        program = self.disk.getProgram( aProgramName )
        base = self.mm.loadProgram( program )
        # todavia no se crear pcb
        aPCB = pcb.PCB(base, self.generatePID() )
        