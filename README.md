# TODO

- scheduling
    - FIFO
    - Prioridad
    - Round Robin (con quantum)
        - FIFO
        - Prioridad
- simplificar cpu
- cpu y clock como thread
- charla entre cpu, irq, y clock
- asignacion de memoria
    - asignacion continua con bloques
    - paginacion
- dispositivos de entrada y salida como thread independientes
    - interrupcion debe saber donde encolar cada pcb
- directorios y archivos
    - acceso mediante rutas
    - carga de programa como lista de bloques, con datos
- filesystem
    - cargable desde disco
    - guardable a disco (serializable)
        - definir formato de archivos y de datos
- kernel.run / kernel.shutdown


## Opcionales

- interfaz grafica
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
