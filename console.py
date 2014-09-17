class Console:
    # muestra el valor por consola, y lo guarda en una lista

    def __init__(self):
        self.lines = []

    def addLine(self, aLine):
        self.lines.append(aLine)
        print (aLine)
