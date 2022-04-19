from src.classes.Node import Node
from src.classes.SymbolTable import SymbolTable

class Assignment(Node):
    #Override
    def Evaluate(self):
        node1 = self.children[0].variant
        node2 = self.children[1].Evaluate()
        SymbolTable.setSymbol(node1, node2)
        return
