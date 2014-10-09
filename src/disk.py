import logging

class Disk:
    # guarda una lista de programas, y busca un programa en la lista

    def __init__(self):
        self.programs = []

    def addProgram(self, aProgram):
        logging.debug( "disk.addProgram()" )
        self.programs.append(aProgram)

    def getProgram(self, aProgramName):
        ## busca el programa en la lista de programas
        logging.debug( "disk.getProgram()" )
        for program in self.programs:
            if program.name == aProgramName:
                return (program)
