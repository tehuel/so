import logging
logging.debug( "class" )

class Scheduler:
    
    def __init__(self):
        self.rpq = []

    def add (self, aPCB):
        logging.info( "scheduler: pcb added to queue" )
        self.rpq.insert(0, aPCB)

    def get (self):
        logging.debug( "scheduler: pcb returned" )
        return self.rpq.pop()
