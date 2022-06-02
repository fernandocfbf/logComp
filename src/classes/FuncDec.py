from src.classes.Node import Node
from src.classes.FuncTable import FuncTable

class FuncDec(Node):
    #@Override
    def Evaluate(self, st):
        print("THERE -> ", self.children[0].children[0][0].variant)
        print("THERE1 -> ", self.children[0].children[0][1])
        FuncTable.createFunction(self.children[0].children[0][0].variant, self.children[0].children[0][1], self)
        print()
        return