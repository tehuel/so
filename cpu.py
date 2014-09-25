import pcb

class CPU:
    
    def __init__(self):
        self.currentPCB = False
        
    def loadPCB(self, aPCB):
        self.currentPCB = aPCB
        
    def isIdle(self):
        return ( not isinstance(self.currentPCB, pcb.PCB) )
