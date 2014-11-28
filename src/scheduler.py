import logging

logger = logging.getLogger(__name__)

class Scheduler:
    
    def __init__(self):
        self.rpq = []

class FIFO_Scheduler(Scheduler):
    
    def add(self, aPCB):
        self.rpq.insert(0, aPCB)
        
    def get (self):
        if ( self.rpq ):
            return self.rpq.pop()
        else:
            return None
            
    def kill (self):
        pass

class Priority_Scheduler(Scheduler):
    
    def add(self, aPCB, aPriority = 0):
        
        # priorizo el pcb
        # esto ya puede venir desde afuera
        aPCB.info = aPriority
        
        #lo agrego a la lista
        self.rpq.append(aPCB)
        
        #ordeno la lista de priorizados
        self.rpq = sorted( self.rpq, key=self.getPriority )

    def get(self):
        return self.rpq.pop()
        
    def kill (self, aPCB):
        # elimino el pid de la lista de pids priorizados
        pass
    
    def getPriority(self, aPCB):
        return aPCB.info

if __name__ == "__main__":
    
    import pcb
    
    logging.basicConfig(level=logging.INFO)
    
    sch = Priority_Scheduler()
    
    sch.add( pcb.PCB(0, 1, 11), 3)
    sch.add( pcb.PCB(0, 1, 22), 2 )
    sch.add( pcb.PCB(0, 1, 33) )
    sch.add( pcb.PCB(0, 1, 44), 1 )
    sch.add( pcb.PCB(0, 1, 55), 2 )

    print sch.rpq
    
    print ( sch.get().pid )
    print ( sch.get().pid )
    print ( sch.get().pid )