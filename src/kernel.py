import pcb

class Kernel:

    def __init__(self, aDisk, aMMU, aCPU, aIRQ, aScheduler, aClock, aConsole):
        self.lastPID = 0
        self.disk = aDisk
        self.mmu = aMMU
        self.cpu = aCPU
        self.irq = aIRQ
        self.scheduler = aScheduler
        self.clock = aClock
        self.console = aConsole
        
        #initialize
        self.irq.setKernel(self)
        self.clock.setKernel(self)
        self.cpu.setKernel(self)
        
    def generatePID(self):
        self.lastPID += 1
        return self.lastPID

    def execute(self, aProgramName):
        #obtengo el programa del disco, lo paso a memoria, y creo el pcb correspondiente
        program = self.disk.getProgram( aProgramName )
        base = self.mmu.loadProgram( program )
        size = len(program.instructions)
        aPCB = pcb.PCB(base, size, self.generatePID() )
        
        #agrego el pcb a la lista de pcbs
        self.scheduler.add( aPCB )
        