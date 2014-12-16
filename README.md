# TODO

- directorios y archivos
    - acceso mediante rutas
    - carga de programa como lista de bloques, con datos
- kernel.run / kernel.shutdown
- cpu y clock como thread
- ejecutar instrucciones de IO
- dispositivos de IO como thread independientes
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

- asignacion de memoria
    - asignacion continua con bloques
    - paginacion
