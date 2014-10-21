import logging

logger = logging.getLogger(__name__)

class Scheduler:
    
    def __init__(self):
        self.rpq = []

    def add (self, aPCB):
        self.rpq.insert(0, aPCB)

    def get (self):
        return self.rpq.pop()
