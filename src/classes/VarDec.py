from src.classes.Node import Node
from src.classes.SymbolTable import SymbolTable

class VarDec(Node):
    #@Override
    def Evaluate(self, st):
        for children in self.children:
            SymbolTable.create(children)
        return