class Console:
    # muestra el valor por consola, y lo guarda en una lista

    def __init__(self):
        self.lines = []
        self.log = []
        
    def toConsole(self, aLine):
        self.lines.append( aLine )
        print (aLine)
        
    def toLog(self, aLogLine, aLogLevel = 0):
        self.log.append ( aLogLine )
        print "LOG: ", aLogLine
