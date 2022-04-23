from src.classes.Node import Node

class If(Node):
    
    #Override
    def Evaluate(self):
        if self.children[0].Evaluate():
            return self.children[1].Evaluate()
        elif len(self.children) > 2:
            self.children[2].Evaluate()