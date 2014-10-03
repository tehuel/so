import pcb

class Kernel:

    def __init__(self, aConsole, aDisk, aMMU, aScheduler):
        self.lastPID = 0
        self.console = aConsole
        self.disk = aDisk
        self.mmu = aMMU
        self.scheduler = aScheduler
        
    def generatePID(self):
        self.lastPID += 1
        return self.lastPID

    def execute(self, aProgramName):
        #obtengo el programa del disco, lo paso a memoria, y creo el pcb correspondiente
        program = self.disk.getProgram( aProgramName )
        base = self.mm.loadProgram( program )
        aPCB = pcb.PCB(base, self.generatePID() )

        self.scheduler.add( aPCB )