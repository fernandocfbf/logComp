from src.classes.Node import Node
from src.classes.SymbolTable import SymbolTable
class Return(Node):

    #Override
    def Evaluate(self):
        return