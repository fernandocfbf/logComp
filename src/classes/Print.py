from src.classes.Node import Node
from src.classes.SymbolTable import SymbolTable
class Print(Node):

    #Override
    def Evaluate(self):
        print(self.children[0].Evaluate())
        return