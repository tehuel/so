class Kernel:
    # crea procesos

    def __init__(self, aConsole, aDisk):
        self.console = aConsole
        self.disk = aDisk

    def execute(self, aProgramName):
        #obtengo el programa del disco, lo paso a memoria, y creo el dcb correspondiente
        program = self.disk.getProgram( aProgramName )
        program.execute(self.console)
