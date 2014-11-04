import logging

logger = logging.getLogger(__name__)

def InterruptionStart():
    #print("Interruption Start")
    pass
        
class Interruption:
    def __init__(self, anInterruptionRoutine):
        self.routine = anInterruptionRoutine
    
    def execute(self):
        self.routine
        

class IRQ:
    
    def __init__(self):
        self.cpu = None
        self.scheduler = None
        self.queue = []
    
    def setCPU(self, aCPU):
        self.cpu = aCPU
    
    def setScheduler(self, aScheduler):
        self.scheduler = aScheduler
        
    def raiseInterruption(self, anInterruption):
        self.queue.insert( 0, anInterruption )
        
    def processInterruption(self):
        self.queue.pop().execute()
