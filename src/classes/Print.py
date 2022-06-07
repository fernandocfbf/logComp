from src.classes.Node import Node
from src.classes.SymbolTable import SymbolTable
class Print(Node):

    #Override
    def Evaluate(self, st):
        print(self.children[0].Evaluate(st)[1])
        return