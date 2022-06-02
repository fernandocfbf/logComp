from src.classes.Node import Node

class While(Node):
    
    #Override
    def Evaluate(self, st):
        while self.children[0].Evaluate()[1]:
            self.children[1].Evaluate()