import logging

class Clock:
        
    def __init__(self, aCPU):
        self.cpu = aCPU
        
    def tick(self):
        # indico a cpu que arranque
        #proceso interrupciones y cambios de contexto
        logging.debug( "clock.tick()" )
        
        self.cpu.fetch()

    def run(self):
        # TODO: write code...
        #sleep(1)
        #self.tick()
        logging.debug( "clock.run()" )
        pass