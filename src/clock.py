import time

import logging

logger = logging.getLogger(__name__)

class Clock:
        
    def __init__(self, aCPU):
        self.counter = 1
        self.cpu = aCPU
        
    def tick(self):
        logger.debug( "tick( %s )", self.counter )
        self.counter = self.counter + 1
        self.cpu.fetch()

    def run(self):
        logger.debug( "clock started" )
        while ( True ):
            time.sleep(3)
            self.tick()