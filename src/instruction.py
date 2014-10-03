class Instruction:

    def __init__(self, aText):
        self.text = aText

    def execute(self, console):
        console.toConsole(self.text)
