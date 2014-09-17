from instruction import *
from program import *
from console import *
from memory import *
from memorymanager import *
from disk import *
from kernel import *
from pcb import *
from cpu import *
from scheduler import *
from quantum import *
from iodevice import *

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
