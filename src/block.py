import logging

logger = logging.getLogger(__name__)

class Block:
    
    #las ids de los bloques aumentan secuencialmente
    counter = 0
    
    def __init__(self, aStart, aSize):
        self.start = aStart
        self.size = aSize
        self.end = self.start+self.size-1
        self.id = self.getID()
        self.content = None

    def __repr__(self):
        return "#{0}({1}/{2})({3}):{4}".format(self.id, self.start, self.end, self.size, self.content)
        
    def getID(self):
        Block.counter += 1
        return Block.counter
        
    def resize(self, aStart, aSize):
        self.start = aStart
        self.size = aSize
        self.end = self.start+self.size-1
        
    def isNextTo(self, aBlock):
        return self.start == aBlock.end+1

if __name__ == "__main__":
    
    logging.basicConfig(level=logging.DEBUG)