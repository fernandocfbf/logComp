from src.classes.Node import Node
class IntVal(Node):

    #@Override
    def Evaluate(self):
        return tuple("int", self.variant)