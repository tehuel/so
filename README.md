# TODO

- charla entre cpu, irq, y clock
- ejecutar realmente las instrucciones
- asignacion de memoria
    - asignacion continua con bloques
    - paginacion
- directorios y archivos
    - acceso mediante rutas
    - carga de programa como lista de bloques, con datos
- kernel.run / kernel.shutdown
- cpu y clock como thread
- simplificar cpu
- ejecutar instrucciones de IO
- dispositivos de entrada y salida como thread independientes
    - interrupcion debe saber donde encolar cada pcb

## Opcionales

- interfaz grafica
- filesystem
    - cargable desde disco
    - guardable a disco (serializable)
        - definir formato de archivos y de datos
    - INODE
- shell comunicable con filesystem
    - ls
    - mmkdir
    - rm

# IN PROGRESS

# DONE

- impementar todas las interupciones
- interrupciones por configuracion
    - no metodos sino rutinas configurables
- manejar cambios de pc en cpu
    - aumentar pcb por cada instruccion ejecutada
    - controlar end
- scheduling
    - FIFO
    - Prioridad
    - Round Robin (con quantum)
