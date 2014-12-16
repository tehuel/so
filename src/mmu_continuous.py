from block import *
import logging

logger = logging.getLogger(__name__)
        
class MMU:
    
    def __init__(self, aMemory):
        self.memory = aMemory
        self.blocks = []
        
        # creo el primer bloque
        self.blocks.append( Block(0, self.memory.size) )

    def __repr__(self):
        return "Blocks: {0}\n{1}".format( len(self.blocks), self.blocks )
        
    def addBlock(self, aBlock):
        self.blocks.append(aBlock)
        self.blocks = sorted(self.blocks, key=lambda block: block.start)    #ordeno los bloques por su posicion inicial
        
    def deleteBlock(self, aBlock):
        self.blocks.remove(aBlock)
    
    def splitBlock(self, aBlock, aSize):
        newBlock = Block(aBlock.start + aSize, aBlock.size - aSize)
        self.addBlock(newBlock)
        aBlock.resize(aBlock.start, aSize)
        
        return aBlock
        
    def joinBlocks(self, aBlock, anotherBlock):
        #primero compruebo que sean vecinos
        if ( aBlock.isNextTo(anotherBlock) or anotherBlock.isNextTo(aBlock) ):
            
            if aBlock.start < anotherBlock.start:
                aBlock.resize(aBlock.start, aBlock.size + anotherBlock.size)
            else:
                aBlock.resize(anotherBlock.start, aBlock.size + anotherBlock.size)
                
            self.deleteBlock(anotherBlock)
            
    def getFreeMemory(self):
        memory = 0
        for b in self.blocks:
            if b.content == None:
                memory += b.size
        return memory
    
    def compactMemory(self):
        pass
    
    def getFreeBlock(self, size):
        #elijo el primer bloque vacio
        freeBlock = None
        for i in self.blocks:
            if (i.size > size and i.content==None):
                freeBlock = i
                return self.splitBlock( freeBlock, size )
        

if __name__ == "__main__":
    
    logging.basicConfig(level=logging.DEBUG)
    
    import memory
    
    mem = memory.Memory(16)
    
    mmu = MMU(mem)
    
    print mmu
    print "Free Memory: " + str( mmu.getFreeMemory() )
    print "----"
    
    mmu.getFreeBlock(10).content = "Algo"
    print mmu
    print "Free Memory: " + str( mmu.getFreeMemory() )
    print "----"

    mmu.getFreeBlock(4).content = "Usado"
    print mmu
    print "Free Memory: " + str( mmu.getFreeMemory() )
    print "----"
