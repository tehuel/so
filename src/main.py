import startup
from devicemanager import *
from kernel import *

import logging

logging.basicConfig(level=logging.INFO)


#creo todos los dispositivos
dm = DeviceManager()

# genero la lista de programas
prg1 = startup.generateProgram( "PRG1", 5 )
prg2 = startup.generateProgram( "PRG2", 10 )

#agrego los programas al disco
dm.disk.addProgram(prg1)
dm.disk.addProgram(prg2)

# creo un kernel con sus dispositivos
k = Kernel( dm )

# ejecuto varios programas
k.execute("PRG1")
k.execute("PRG2")
k.execute("PRG1")
k.execute("PRG2")

# inicio el clock del procesador
dm.clock.run()
