from src.classes.Node import Node
from src.classes.FuncTable import FuncTable

class FuncDec(Node):
    #@Override
    def Evaluate(self, st):
        print(self.children[0].children[0][0].variant)
        print(self.children[0].children[0][1])
        FuncTable.createFunction(self.children[0].children[0][0].variant, self.children[0].children[0][1], self)
        return