import logging
import random

from instruction import *
from program import *
from devicemanager import *

def generateProgram( aName, aSize ):
    prg = Program( aName )
    for r in range(aSize):
        prg.addInstruction( Instruction(r) )
    return prg

