from src.classes.Node import Node
class IntVal(Node):

    #@Override
    def Evaluate(self, st):
        return ("int", self.variant)