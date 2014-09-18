class Instruction:

    def __init__(self, aText):
        self.text = aText

    def execute(self, console):
        console.say(self.text)
