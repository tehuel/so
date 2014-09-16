class Console:
    # muestra el valor por consola, y lo guarda en una lista

    def __init__(self):
        self.lines = []

    def addLine(self, aLine):
        self.lines.append(aLine)
        print (aLine)

class Disk:
    # guarda una lista de programas, y busca un programa en la lista

    def __init__(self):
        self.programs = []

    def addProgram(self, aProgram):
        self.programs.append(aProgram)

    def getProgram(self, aProgramName):
        ## busca el programa en la lista de programas
        for program in self.programs:
            if program.name == aProgramName:
                return (program)

class MemoryManager:
    # maneja una memoria
    # guarda todas las instrucciones de un programa, devolviendo posicion inicial
    # lee una instruccion en una posicion determinada

    def __init__(self, aMemory):
        self.memory = aMemory
        self.lastPosition = 0

    def loadProgram(self, aProgram):
        # agarra lista de instrucciones del programa y los guarda en memoria
        # devuelve posicion inicial en memoria
        
        self.initialPosition = self.lastPosition
        
        for instruction in aProgram.instructions:
            self.memory.write( instruction )
            self.lastPosition += 1
            print ( self.initialPosition )
            return ( self.initialPosition )

    def getInstruction(self, aCellNumber):
        # lee una posicion de memoria

        self.foundInstruction = self.memory.read( aCellNumber )

        return ( self.foundInstruction )

class Memory:
    # guarda una lista de instrucciones

    def __init__(self):
        self.memoryCells = []

    def read(self, aCellNumber):
        self.memoryCells[ aCellNumber ]

    def write(self, anInstruction):
        self.memoryCells.append ( anInstruction )

class PCB:
    # es creado por el kernel al ejecutar un programa

    def __init__( self, memoryPos, aPID ):
        self.pc = 0
        self.memoryPos = memoryPos
        self.state = "READY"
        self.pid = aPID

class Instruction:

    def __init__(self, aText):
        self.text = aText

    def execute(self, console):
        console.addLine(self.text)

class Program:
    # es una lista de instrucciones, con un nombre

    def __init__(self, aName):
        self.name = aName
        self.instructions = []

    def addInstruction(self, anInstruction):
        self.instructions.append(anInstruction)

    def execute(self, console):
        for inst in self.instructions:
            inst.execute(console)

class Kernel:
    # crea procesos

    def __init__(self, aConsole, aDisk):
        self.console = aConsole
        self.disk = aDisk

    def execute(self, aProgramName):
        #obtengo el programa del disco, lo paso a memoria, y creo el dcb correspondiente
        program = self.disk.getProgram( aProgramName )
        program.execute(self.console)


insa = Instruction("A")
insb = Instruction("B")
insc = Instruction("C")

prg1 = Program( "PRG1" )
prg1.addInstruction( insa )
prg1.addInstruction( insb )
prg1.addInstruction( insc )
prg1.addInstruction( insb )
prg1.addInstruction( insa )

prg2 = Program( "PRG2" )
prg2.addInstruction( insb )
prg2.addInstruction( insb )

hdd = Disk()
hdd.addProgram( prg1 )
hdd.addProgram( prg2 )

c = Console()
m = Memory()
mm = MemoryManager ( m )
k = Kernel( c, hdd )

mm.loadProgram( prg1 )
mm.loadProgram( prg2 )
    


