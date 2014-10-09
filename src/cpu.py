import logging

class CPU:
    
    def __init__(self):
        # inicializacion de cpu
        logging.debug( "cpu.init" )
        self.pcb = None
    
    def setIRQ(self, aIRQ):
        logging.debug( "cpu.setIRQ()" )
        self.irq = aIRQ
    
    def fetch(self):
        #levanto excepcion de start
        logging.debug( "cpu.fetch()" )
        
        if (self.pcb == None):
            self.irq.interruptionStart()
        
        self.execute()
        
        
    def execute(self):
        # TODO: write code...
        logging.debug( "cpu.execute()" )
        #nextInstruction = self.kernel.mmu.getInstruction( self.pcb.base + self.pcb.pc )
        #nextInstruction.execute(self.kernel.console)
        
    def getContext(self):
        # TODO: write code...
        logging.debug( "cpu.getContext()" )
        
    def setContext(self, aPCB):
        logging.debug( "cpu.setContext()" )
        self.pcb = aPCB
