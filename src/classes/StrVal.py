from src.classes.Node import Node
class StrVal(Node):

    #@Override
    def Evaluate(self):
        return ("str", self.variant)