class Clock:
    
    def __init__(self, aCPU):
        self.cpu = aCPU
        
    def tick(self):
        self.cpu.fetch

        #proceso interrupciones
        
    def start(self):
        while ( True ):
            time.sleep(1)
            self.tick
