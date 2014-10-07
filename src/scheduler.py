class Scheduler:
    
    def __init__(self):
        self.rpq = []

    def add (self, aPCB):
        self.rpq.insert(0, aPCB)
        print("scheduler: pcb added to queue", self.rpq)
        
    def get (self):
        print( "scheduler: pcb returned", self )
        return self.rpq.pop()
