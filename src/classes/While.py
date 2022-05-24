from src.classes.Node import Node
from src.classes.CodeGenerator import CodeGenerator

class While(Node):
    
    #Override
    def Evaluate(self):
        CodeGenerator.write("LOOP_{0}".format(self.i))
        
        while self.children[0].Evaluate()[1]:
            self.children[1].Evaluate()