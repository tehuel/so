class Quantum:
    # listado de pcbs
    
    def __init__(self):
        self.queue = []

    def add (self, aPCB):
        self.queue.append(aPCB)