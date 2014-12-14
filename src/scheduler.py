import logging

logger = logging.getLogger(__name__)

class FIFO_Policy:
    
    def add(self, **params):
        scheduler = params['sche']
        aPCB = params['pcb']
        
        #agrego el pcb a la lista
        scheduler.rpq.insert(0, aPCB)
        
        logger.debug('PCB added to FIFO queue. ' + str(aPCB) )
        
class PRIORITY_Policy:
    
    def add(self, **params):
        scheduler = params['sche']
        aPCB = params['pcb']
        aPCB.priority = params['pri']   # asigno prioridad al pcb
        
        #agrego el pcb a la lista y la ordeno por prioridad
        scheduler.rpq.insert(0, aPCB)
        scheduler.rpq = sorted( scheduler.rpq, key=self.getPriority )
        
        logger.debug('PCB added to PRIORIZED queue. ' + str(aPCB) )
        
        
    def getPriority(self, aPCB):
        # criterio de ordenacion
        return aPCB.priority


class Scheduler:
    
    def __init__(self, aPolicy=FIFO_Policy):
        self.rpq = []   #listado de todos los pcbs
        self.policy = aPolicy()
        
        logger.debug('Scheduler Initialized')
        logger.debug( aPolicy )

    def add(self, aPCB, aPriority=0):
        return self.policy.add(pcb=aPCB, pri=aPriority, sche=self)
        
    def get(self):
        # es el mismo get para todas las policies
        if ( self.rpq ):
            logger.debug('returned PCB from queue')
            return self.rpq.pop()
        else:
            logger.debug('queue is EMPTY')
            return None


if __name__ == "__main__":
    
    import pcb
    
    logging.basicConfig(level=logging.DEBUG)
    
    pcb1 = pcb.PCB(0,10,1)
    pcb2 = pcb.PCB(0,10,2)
    pcb3 = pcb.PCB(0,10,3)
    pcb4 = pcb.PCB(0,10,4)
    pcb5 = pcb.PCB(0,10,5)

    print "-- TEST FIFO SCHEDULER --"
    # FIFO Scheduler (default)
    scheduler1 = Scheduler()
    
    scheduler1.add( pcb1 )
    scheduler1.add( pcb2 )
    scheduler1.add( pcb3 )
    scheduler1.add( pcb4 )
    scheduler1.add( pcb5 )
    
    print scheduler1.get()
    print scheduler1.get()
    print scheduler1.get()
    print scheduler1.get()
    print scheduler1.get()
    print scheduler1.get()

    print "-- TEST PRIORITY SCHEDULER --"
    # PRIORITY Scheduler
    scheduler2 = Scheduler( PRIORITY_Policy )
    
    scheduler2.add( pcb1 )
    scheduler2.add( pcb2, 10 )
    scheduler2.add( pcb3 )
    scheduler2.add( pcb4, 20 )
    scheduler2.add( pcb5 )
    
    print scheduler2.get()
    print scheduler2.get()
    print scheduler2.get()
    print scheduler2.get()
    print scheduler2.get()
    print scheduler2.get()

