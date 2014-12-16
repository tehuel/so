import time

import logging

logger = logging.getLogger(__name__)

class Clock:
        
    def __init__(self, aCPU):
        self.counter = 1
        self.cpu = aCPU
        
    def tick(self):
        # inicio ciclo
        print ('------')
        logger.debug( "tick( %s )", self.counter )
        self.counter = self.counter + 1
        
        # ejecuto fetch de cpu
        self.cpu.fetch()
        
        # ejecuto una de las interrupciones
        self.cpu.irq.processInterruption()

    def run(self):
        logger.debug( "clock started" )
        while ( True ):
            time.sleep(1)
            self.tick()