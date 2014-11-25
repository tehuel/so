import logging

logger = logging.getLogger(__name__)

class Interruption:
    # clase padre de las interrupciones. se le pasan rutinas de interrupciones
    
    def __init__(self, anInterruptionType):
        self.interruptionType = anInterruptionType

    def run(self, aScheduler, aCPU):
        self.interruptionType.run( aScheduler, aCPU)

class Start:
    
    def run(self, aScheduler, aCPU):
        logger.debug( "running start interruption" )
        aCPU.setContext( aScheduler.get() )

class Timeout:
    
    def run(self, aScheduler, aCPU):
        logger.debug( "running timeout interruption" )

class End:
    
    def run(self, aScheduler, aCPU):
        logger.debug( "running end interruption" )

class IO:
    
    def run(self, aScheduler, aCPU):
        logger.debug( "running io interruption" )

if __name__ == "__main__":
    
    logging.basicConfig(level=logging.DEBUG)
    
    print "Hola Mundo"
    
    newInterruption = Interruption( Start() )
    newInterruption.run()