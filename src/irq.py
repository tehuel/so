import logging

class IRQ:
    
    def __init__(self):
        # inicializo listado de interrupciones
        pass
    
    def setCPU(self, aCPU):
        self.cpu = aCPU
    
    def setScheduler(self, aScheduler):
        self.scheduler = aScheduler
    
    def interruptionStart(self):
        # interrupcion inicial, le doy un pcb al cpu
        logging.debug( "irq.interruptionStart()" )
        self.cpu.setContext( self.scheduler.get() )

    def interruptionEnd(self):
        # TODO: write code...
        logging.debug( "irq.interruptionEnd()" )

    def interruptionTimeout(self):
        # TODO: write code...
        logging.debug( "irq.interruptionTimeout()" )

    def changeContext(self):
        # cambio de contexto. saco pcb de cpu y pongo siguiente pcb en cpu
        logging.debug( "irq.changeContext()" )
