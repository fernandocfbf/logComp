from src.classes.Node import Node

class While(Node):
    
    #Override
    def Evaluate(self):
        while self.children[0].Evaluate():
            self.children[1].Evaluate()