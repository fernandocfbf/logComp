from src.classes.Node import Node
from src.classes.SymbolTable import SymbolTable
class Block(Node):

    #Override
    def Evaluate(self):
        for children in self.children:
            children.evaluate()
        return