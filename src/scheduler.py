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
    
    def __init__(self):
        self.rpq = {} # diccionario de pcbs
        self.pri = [] # lista de tuplas ordenadas por prioridad
    
    def add(self, aPCB, aPriority = 0):
        #priorizo el PCB y lo agrego a la lista de priorizados
        aPriorizedPCB = ( aPriority, aPCB.pid )
        self.pri.append( aPriorizedPCB )
        
        #ordeno la lista de priorizados
        self.pri = sorted( self.pri, reverse=True, key=lambda priorized: priorized[0] )
        
        # agrego el pcb al diccionario
        self.rpq[aPCB.pid] = aPCB
        
    def get(self):
        
        # de la lista de pids priorizados devuelvo el primero que tenga en el diccionario de pcbs
        item = None
        for i, j in self.pri:
            
            if ( j in self.rpq ):
                item = self.rpq[j]
                del self.rpq[j]
                break
                
        return item
        
    def kill (self, aPCB):
        # elimino el pid de la lista de pids priorizados
        pass

if __name__ == "__main__":
    
    import pcb
    
    logging.basicConfig(level=logging.INFO)
    
    sch = Priority_Scheduler()
    
    sch.add( pcb.PCB(0, 1, 11), 3)
    sch.add( pcb.PCB(0, 1, 22), 2 )
    sch.add( pcb.PCB(0, 1, 33) )
    sch.add( pcb.PCB(0, 1, 44), 1 )
    sch.add( pcb.PCB(0, 1, 55), 2 )

    print sch.pri
    print sch.rpq
    
    print ( sch.get() )
    print ( sch.get() )
    print ( sch.get() )