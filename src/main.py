import logging

logging.basicConfig(level=logging.DEBUG)

from instruction import *
from program import *
from console import *
from kernel import *
from irq import *
from scheduler import *
from pcb import *
from devicemanager import *

insa = Instruction("A")
insb = Instruction("B", True)
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
prg2.addInstruction( insc )

dm = DeviceManager()
dm.disk.addProgram(prg1)
dm.disk.addProgram(prg2)

console = Console()

sch = Scheduler()

irq = IRQ()

k = Kernel( dm, irq, sch, console )

k.execute("PRG1")
k.execute("PRG2")
k.execute("PRG1")
k.execute("PRG2")

dm.clock.run()

#dm.clock.tick()
