class Instruction:

    def __init__(self, aText):
        self.text = aText

    def execute(self, aConsole):
        self.console = aConsole
        self.console.out(self.text)
