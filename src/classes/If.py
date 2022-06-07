from src.classes.Node import Node

class If(Node):
    
    #Override
    def Evaluate(self, st):
        if self.children[0].Evaluate(st):
            return self.children[1].Evaluate(st)
        elif len(self.children) > 2:
            self.children[2].Evaluate(st)