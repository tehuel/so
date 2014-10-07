class IRQ:
    
    def __init__(self):
        # inicializo listado de interrupciones
        pass
    
    def setKernel(self, aKernel):
        self.kernel = aKernel
    
    def interruptionStart(self):
        # interrupcion inicial, le doy un pcb al cpu
        print("irq: interruptionStart", self)
        self.kernel.cpu.setContext( self.kernel.scheduler.get() )

    def interruptionEnd(self):
        # TODO: write code...
        print("irq: interruptionEnd", self)

    def interruptionTimeout(self):
        # TODO: write code...
        print("irq: interruptionTimeout", self)

    def changeContext(self):
        # cambio de contexto. saco pcb de cpu y pongo siguiente pcb en cpu
        print("irq: changeContext", self)
