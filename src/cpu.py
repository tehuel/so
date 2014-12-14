from interruption import *
import logging

logger = logging.getLogger(__name__)

class CPU:
    
    def __init__(self, aMemoryManager):
        # inicializacion de cpu
        logger.debug( "init" )
        self.mmu = aMemoryManager
        self.context = None
        self.irq = None
        self.quantum = None
        self.streak = 0
    
    def setIRQ(self, aIRQ):
        self.irq = aIRQ

    def fetch(self):
        logger.debug( "fetch() started" )

        #levanto excepcion de start
        if (self.context == None):
            
            logger.debug( "start interruption" )
            self.irq.raiseInterruption( Interruption( Start() ) )
            
        else:
        
            #si la instruccion se paso del tamanio del programa
            if (self.context.pc >= self.context.size ):
                logger.debug( "end interruption" )
                self.irq.raiseInterruption( Interruption( End() ) )
            else:
                    
                # obtengo la instruccion
                i = self.mmu.getInstruction( self.context.getNextInstruction() )
                    
                #si la instruccion es de entrada salida
                if ( i.isIO() ):
                    logger.debug( "IO interruption" )
                    self.irq.raiseInterruption( Interruption( IO() ) )
                else:
                    
                    # si la instruccion se paso del quantum
                    if (self.quantum):
                        if ( self.streak > self.quantum ):
                            # interrupcion de timeout
                            logger.info( " ------- TIMEOUT" )
                            self.irq.raiseInterruption( Interruption( Timeout() ) )
                    
                    #ejecuto instruccion
                    self.streak += 1
                    logger.debug( "instruction execution" )
                    #actualizo pcb
                
                #debug: avanzo pcb de todas formas
                self.context.updatePC()
                
        
    def getContext(self):
        logger.debug( "getContext()" )
        return self.context
        
    def setContext(self, aPCB):
        logger.debug( "setContext()" )
        self.context = aPCB
        self.streak = 0
