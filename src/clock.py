class Clock:
        
    def setKernel(self, aKernel):
        self.kernel = aKernel
        
    def tick(self):
        # indico a cpu que arranque
        #proceso interrupciones y cambios de contexto
        print("clock: tick start", self)
        
        self.kernel.cpu.fetch()

    def run(self):
        # TODO: write code...
        #sleep(1)
        #self.tick()
        pass