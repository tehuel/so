class Scheduler:
    
    def __init__(self):
        self.queue = []

    def add (self, aPCB):
        self.queue.append(aPCB)
        
    def get (self):
        return self.queue.remove()