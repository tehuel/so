class CPU:
    
    def __init__(self):
        # inicializacion de cpu
        self.pcb = None
    
    def setIRQ(self, aIRQ):
        self.irq = aIRQ
    
    def fetch(self):
        #levanto excepcion de start
        print("cpu: fetch", self)
        
        if (self.pcb == None):
            self.irq.interruptionStart()
        
        self.execute()
        
        
    def execute(self):
        # TODO: write code...
        print("cpu: execute", self)
        #nextInstruction = self.kernel.mmu.getInstruction( self.pcb.base + self.pcb.pc )
        #nextInstruction.execute(self.kernel.console)
        
    def getContext(self):
        # TODO: write code...
        print("cpu: getContext", self)
        
    def setContext(self, aPCB):
        print("cpu: setContext", self)
        self.pcb = aPCB
