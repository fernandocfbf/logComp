from src.classes.Node import Node
from src.classes.FuncTable import FuncTable

class FuncDec(Node):
    #@Override
    def Evaluate(self, st):
        FuncTable.createFunction(self.children[0].children[0], self.children[0].children[1].variant, self)
        return