import logging

logger = logging.getLogger(__name__)

class Filesystem:
    
    def __init__(self):
        self.root = Directory("root")
        
    def loadFile(self, aPath):
        
        current_folder = self.root
        exploded_path = aPath.split("/")
        exploded_path.reverse()
        
        while ( len(exploded_path) > 1 ):
            
            directory_to_find = exploded_path.pop()
            current_folder = current_folder.subdirectories[ directory_to_find ]
                
        #cuando ya tengo la ultima carpeta creo el archivo
        return current_folder.getFile( exploded_path.pop() )

    
    def saveFile(self, aFile, aPath = None):
        
        current_folder = self.root
        
        if ( aPath != None ):
            exploded_path = aPath.split("/")
            exploded_path.reverse()
            
            while ( len(exploded_path) > 0 ):
                
                directory_to_find = exploded_path.pop()
                
                # si la carpeta no existe la creo
                if ( not current_folder.subdirectories.has_key(directory_to_find) ):
                    new_directory = Directory(directory_to_find)
                    current_folder.addSubdirectory( new_directory )
                    logger.debug("folder ", new_directory, "added" )
                    
                # preparo la proxima carpeta del path
                current_folder = current_folder.subdirectories[ directory_to_find ]
                
        #cuando ya tengo la ultima carpeta creo el archivo
        current_folder.addFile( aFile )
        logger.debug("added a file to folder ", current_folder )
    
    def printTree(self):
        self.root.printContent()
        
    

class Directory:
    
    def __init__(self, aDirectoryName):
        self.name = aDirectoryName
        self.subdirectories = {}
        self.files = {}
        self.depth = 0
        self.parent = None
        
    def addSubdirectory(self, aDirectory):
        aDirectory.setParent(self)
        aDirectory.setDepth(self.depth+1)
        self.subdirectories[aDirectory.name] = aDirectory
        
    def setParent(self, aDirectory):
        self.parent = aDirectory
        
    def setDepth(self, aDepthNumber):
        self.depth = aDepthNumber
        
    def addFile(self, aFile):
        self.files[aFile.name] = aFile
        
    def getFile(self, aFileName):
        if ( aFileName in self.files):
            return self.files[aFileName]
        else:
            return False
        
    def printContent(self):
        
        if ( self.parent == None ):
            print("/" + self.name)
        else:
            print( "|"*self.depth + self.name)

        for directory in self.subdirectories.itervalues():
            directory.printContent()
            
        for file in self.files.itervalues():
            print ( "|"*self.depth+  file.name)
            
        

class File:
    
    def __init__(self, aFileName):
        self.name = aFileName


if __name__ == "__main__":
    
    # logging.basicConfig(level=logging.DEBUG)
    
    #algunas pruebas
    f1 = File("file.exe")
    f2 = File("file.bat")
    f3 = File("file.com")
    
    fs = Filesystem()
    fs.saveFile(f1, "a/path")
    fs.saveFile(f2, "a/path/inside")
    fs.saveFile(f1, "another/path")
    fs.saveFile(f3, "another")
    
    fs.printTree()
    
    print ( fs.loadFile("a/path/file.exe") )
    print ( fs.loadFile("a/path/virus.exe") )
    
