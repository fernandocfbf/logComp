from src.classes.Node import Node
from src.classes.SymbolTable import SymbolTable

class Identifier(Node):

    #Override
    def Evaluate(self):
        return SymbolTable.getSymbol(self.variant)
