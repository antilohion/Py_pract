#Small tabulation training

class Indenter:
    def __init__(self):
        self.level = 0
        print('in')

    def __enter__(self):
        self.level += 1
        print('enter')
        
    def print(self,text):
        print(' ' * self.level + text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -=1
        print('ex')

indent=Indenter()

with indent:
    indent.print('1')
    with indent:
        indent.print('2')
        with indent:
            indent.print('3')
    indent.print('4')
