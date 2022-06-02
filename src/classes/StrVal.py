from src.classes.Node import Node
class StrVal(Node):

    #@Override
    def Evaluate(self, st):
        return ("str", self.variant)