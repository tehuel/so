import logging

logger = logging.getLogger(__name__)

class CPU:
    
    def __init__(self, aMemoryManager):
        # inicializacion de cpu
        logger.debug( "init" )
        self.mmu = aMemoryManager
        self.context = None
        self.irq = None
    
    def setIRQ(self, aIRQ):
        self.irq = aIRQ
    
    def fetch(self):
        logger.debug( "fetch()" )

        #levanto excepcion de start
        if (self.context == None):
            logger.info( "IRQ-Interrupcion start" )
            self.irq.interruptionStart()
        else:
        
            #si la instruccion se paso del tamanio del programa
            if (self.context.pc >= self.context.size ):
                logger.info( "IRQ-Interrupcion end" )
                self.irq.interruptionEnd()
            else:
                    
                # obtengo la instruccion
                i = self.mmu.getInstruction( self.context.getNext() )
                    
                #si la instruccion es de entrada salida
                if ( i.isIO() ):
                    logger.info( "IRQ-Interrupcion IO" )
                    self.irq.interruptionIO()
                else:
                    #ejecuto instruccion
                    logger.info( "ejecuto Instruccion" )
                    #actualizo pcb
                
                #debug: avanzo pcb de todas formas
                self.context.updatePC()
                
        
    def getContext(self):
        logger.debug( "getContext()" )
        
    def setContext(self, aPCB):
        self.context = aPCB
        logger.debug( "setContext( PID %s )", self.context.pid )
