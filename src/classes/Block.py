from src.classes.Node import Node
from src.classes.SymbolTable import SymbolTable
class Block(Node):

    #Override
    def Evaluate(self, st):
        for children in self.children:
            children.Evaluate()
        return