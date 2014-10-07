from instruction import *
from program import *
from console import *
from disk import *
from memory import *
from mmu import *
from kernel import *
from clock import *
from cpu import *
from irq import *
from scheduler import *
from iodevice import *
from pcb import *

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
prg2.addInstruction( insb )

hdd = Disk()
hdd.addProgram( prg1 )
hdd.addProgram( prg2 )

console = Console()

mem = Memory()
mmu = MMU(mem)

cpu = CPU()

sch = Scheduler()

irq = IRQ()

clock = Clock()

k = Kernel( hdd, mmu, cpu, irq, sch, clock, console )

k.execute("PRG1")

clock.tick()