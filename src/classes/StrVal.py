from src.classes.Node import Node
class StrVal(Node):

    #@Override
    def Evaluate(self):
        return tuple("str", self.variant)