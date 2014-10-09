class Clock:
        
    def __init__(self, aCPU):
        self.cpu = aCPU
        
    def tick(self):
        # indico a cpu que arranque
        #proceso interrupciones y cambios de contexto
        print("clock: tick start", self)
        
        self.cpu.fetch()

    def run(self):
        # TODO: write code...
        #sleep(1)
        #self.tick()
        pass